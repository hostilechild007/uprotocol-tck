# -------------------------------------------------------------------------
#
# Copyright (c) 2024 General Motors GTO LLC
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# SPDX-FileType: SOURCE
# SPDX-FileCopyrightText: 2024 General Motors GTO LLC
# SPDX-License-Identifier: Apache-2.0
#
# -------------------------------------------------------------------------

import socket
import selectors
import threading
import logging
import re
from collections import defaultdict
from typing import Dict, List, Union
from google.protobuf.any_pb2 import Any
from multimethod import multimethod

from uprotocol.proto.uattributes_pb2 import UAttributes, UPriority, UMessageType
from uprotocol.proto.uri_pb2 import UUri, UAuthority, UEntity, UResource
from uprotocol.proto.umessage_pb2 import UMessage
from uprotocol.proto.ustatus_pb2 import UStatus
from uprotocol.transport.ulistener import UListener
from uprotocol.cloudevent.cloudevents_pb2 import CloudEvent
from uprotocol.proto.uuid_pb2 import UUID
from uprotocol.proto.upayload_pb2 import UPayload, UPayloadFormat
from uprotocol.proto.ustatus_pb2 import UCode
from uprotocol.transport.builder.uattributesbuilder import UAttributesBuilder
from uprotocol.rpc.rpcmapper import RpcMapper
from uprotocol.uri.serializer.longuriserializer import LongUriSerializer
from uprotocol.uri.serializer.microuriserializer import MicroUriSerializer
from uprotocol.uri.serializer.uriserializer import UriSerializer

from up_client_socket_python.transport_layer import TransportLayer
from up_client_socket_python.utils.socket_message_processing_utils import receive_socket_data, convert_bytes_to_string, convert_json_to_jsonstring, convert_jsonstring_to_json, convert_str_to_bytes, protobuf_to_base64, base64_to_protobuf_bytes, send_socket_data, is_close_socket_signal, is_serialized_protobuf, is_json_message, is_serialized_string
from protobuf_builders.uauthoritybuilder import UAuthorityBuilder
from protobuf_builders.uentitybuilder import UEntityBuilder
from protobuf_builders.upayloadbuilder import UPayloadBuilder
from protobuf_builders.uresourcebuilder import UResourceBuilder
from protobuf_builders.uuribuilder import UUriBuilder

from up_client_socket_python.utils.grammar_parsing_utils import get_priority, get_umessage_type
from up_client_socket_python.utils.constants import SEND_COMMAND, REGISTER_LISTENER_COMMAND, UNREGISTER_LISTENER_COMMAND, INVOKE_METHOD_COMMAND, LONG_URI_SERIALIZE, LONG_URI_DESERIALIZE, MICRO_URI_SERIALIZE, MICRO_URI_DESERIALIZE,  LONG_URI_SERIALIZE_RESPONSE, LONG_URI_DESERIALIZE_RESPONSE, MICRO_URI_SERIALIZE_RESPONSE, MICRO_URI_DESERIALIZE_RESPONSE


from logger.logger import logger

class SocketTestManager():
    """
    Validates data received from Test Agent 
    Example: can validate different message-passing mediums (ex: up-client-socket-xxx, zenoh, ...) 
    from different devices.

    Test Manager acts as a server that interoperable (ex: Java, C++, Rust, etc.) Test Agents will connect to.
    These connections will later do be used for stress testing, testing the latencies in sending messages in a high
    message passing sending rates, the size of messages, and the implementation of the core SDK

    Assumption: For every connection between Test Agent (TA) and Test Manager (TM), 
    message passing is blocking/sychronous 

    """
    def __init__(self, ip_addr: str, port: int, utransport: TransportLayer) -> None:
        """Starts Test Manager by creating the server and accepting Test Agent client socket connections

        Args:
            ip_addr (str): Test Manager's ip address
            port (int): Test Manager's port number
            utransport (TransportLayer): Real message passing medium (sockets)
        """

        self.received_umessage: UMessage = None

        # Lowlevel transport implementation (ex: Ulink's UTransport, Zenoh, etc).
        self.utransport: TransportLayer = utransport

        # Bc every sdk connection is unqiue, map the socket connection.
        self.sdk_to_test_agent_socket: Dict[str, socket.socket] = defaultdict(socket.socket)
        self.sdk_to_received_ustatus: Dict[str, UStatus] = defaultdict(lambda: None)  # maybe thread safe
        self.sdk_to_received_ustatus_lock = threading.Lock()

        self.sdk_to_test_agent_socket_lock = threading.Lock()
        
        self.sdk_to_serializer_translation = defaultdict(lambda: None)
        self.sdk_to_serializer_translation_lock = threading.Lock()

        self.sock_addr_to_sdk: Dict[tuple[str, int], str] = defaultdict(str) 

        # Creates test manager socket server so it can accept connections from Test Agents.
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Binds to socket server.
        self.server.bind((ip_addr, port))  
        # Puts the socket into listening mode.
        self.server.listen(100)  
        
        self.server.setblocking(False)
        
        # Selector allows high-level and efficient I/O multiplexing, built upon the select module primitives.
        self.selector = selectors.DefaultSelector()
        # Register server socket so selector can monitor for incoming client conn. and calls provided callback()
        self.selector.register(self.server, selectors.EVENT_READ, self.__accept)
    
    def __accept(self, server: socket.socket):
        """Accepts Test Agent client socket connect requests and listens for incoming data from the new TA conn.

        Args:
            server (socket.socket): Test Manager server
        """
        ta_socket, addr = server.accept() 
        logger.info(f'accepted conn. {addr}')
        
        # Never wait for the operation to complete. 
        # So when call send(), it will put as much data in the buffer as possible and return.
        ta_socket.setblocking(False)
        # Register client socket so selector can monitor for incoming TA data and calls provided callback()
        self.selector.register(ta_socket, selectors.EVENT_READ, self.__receive_from_test_agent)
    
    def __receive_from_test_agent(self, ta_socket):
        """handles incoming json data from Test Agent

        Args:
            ta_socket (socket.socket): <SDK> Test Agent 
        """

            
        recv_data: bytes = receive_socket_data(ta_socket)
        
        # if client socket closed connection, then close on server endpoint too
        if is_close_socket_signal(recv_data):
            try: 
                ta_addr: tuple[str, int] = ta_socket.getpeername()
                sdk: str = self.sock_addr_to_sdk[ta_addr] 
                
                self.close_ta_socket(sdk)
                
                del self.sock_addr_to_sdk[ta_addr]
            except OSError as oserr:
                logger.error(oserr)
            return

        if is_json_message(recv_data): 
            json_str: str = convert_bytes_to_string(recv_data) 

            # in case if json messages are concatenated, we are splitting the json data and handling it separately
            data_within_json : List[str]= re.findall('{(.+?)}', json_str)  # {json, action: ..., messge: "...."}{json, action: status messge: "...."}
            for recv_json_data in data_within_json:
                json_msg: Dict[str, str] = convert_jsonstring_to_json("{" + recv_json_data + "}")
                self.__handle_recv_json_message(json_msg, ta_socket)
            
            return
        
        
        ## NOTE NEED todo some checking if sent is the same as the received but translated back -> THEN save 
        # Map: (sdk, expected response bytes/str/proto)
        if is_serialized_protobuf(recv_data):
            # should expect this after sending to TA the string version
            
            ta_addr: tuple[str, int] = ta_socket.getpeername()
            sdk: str = self.sock_addr_to_sdk[ta_addr]
            
            uuri: UUri = RpcMapper.unpack_payload(Any(value=recv_data), UUri)
            self.__save_serializer_translation(sdk, uuri)
            return
            
        if is_serialized_string(recv_data):
            ta_addr: tuple[str, int] = ta_socket.getpeername()
            sdk: str = self.sock_addr_to_sdk[ta_addr]
            
            uuri_serialized: str = recv_data.decode()
            self.__save_serializer_translation(sdk, uuri_serialized)
            return
        
        '''if is_micro_uri_serialized(recv_data):
            print("is_micro_uri_serialized")
            ta_addr: tuple[str, int] = ta_socket.getpeername()
            sdk: str = self.sock_addr_to_sdk[ta_addr]
            
            self.__save_serializer_translation(sdk, recv_data)
            return'''
    
    def __handle_recv_protobuf(self, received_data: bytes):
        pass
    

    def __handle_recv_json_message(self, json_msg: Dict[str, str], ta_socket: socket.socket):
        """Runtime Handler for different type of incoming json messages

        Args:
            json_msg (Dict[str, str]): received json data
            ta_socket (socket.socket): Test Agent socket connection

        Raises:
            Exception: if dont recognize certain received json messages
        """
        if "SDK_name" in json_msg:
            sdk: str = json_msg["SDK_name"].lower().strip()
            
            ta_addr: tuple[str, int] = ta_socket.getpeername()
            self.sock_addr_to_sdk[ta_addr] = sdk
            
            # Store new SDK's socket connection
            self.sdk_to_test_agent_socket_lock.acquire()
            self.sdk_to_test_agent_socket[sdk] = ta_socket
            self.sdk_to_test_agent_socket_lock.release()
            
            logger.info(f"Initialized new client socket! {sdk}")
            return

        ta_addr: tuple[str, int] = ta_socket.getpeername()
        sdk: str = self.sock_addr_to_sdk[ta_addr]

        if "action" in json_msg and json_msg["action"] == "uStatus":
            # update status if received UStatus message
            umsg_base64: str = json_msg["message"]
            protobuf_serialized_data: bytes = base64_to_protobuf_bytes(umsg_base64)  
            status: UStatus = RpcMapper.unpack_payload(Any(value=protobuf_serialized_data), UStatus)
            
            self.__save_status(sdk, status)
        
        elif "action" in json_msg and json_msg["action"] == "onReceive":
            # update status if received UStatus message
            umsg_base64: str = json_msg["message"]
            protobuf_serialized_data: bytes = base64_to_protobuf_bytes(umsg_base64)  
            onreceive_umsg: UMessage = RpcMapper.unpack_payload(Any(value=protobuf_serialized_data), UMessage)

            self.received_umessage = onreceive_umsg

            logger.info("---------------------OnReceive response from Test Agent!----------------------------")
            logger.info(onreceive_umsg)
            logger.info("------------------------------------------------------------------------------------")

        elif "action" in json_msg and json_msg["action"] == LONG_URI_SERIALIZE_RESPONSE:
            # "message" is a string
            uuri_serialized: str = json_msg["message"]
            self.__save_serializer_translation(sdk, uuri_serialized)
            
        elif "action" in json_msg and (json_msg["action"] == LONG_URI_DESERIALIZE_RESPONSE or json_msg["action"] == MICRO_URI_DESERIALIZE_RESPONSE):
            uuri_base64: str = json_msg["message"]
            protobuf_serialized_data: bytes = base64_to_protobuf_bytes(uuri_base64)  
            uuri: UUri = RpcMapper.unpack_payload(Any(value=protobuf_serialized_data), UUri)
            self.__save_serializer_translation(sdk, uuri)
            
        elif "action" in json_msg and json_msg["action"] == MICRO_URI_SERIALIZE_RESPONSE:
            uuri_serialized_s: str = json_msg["message"]
            uuri_serialized: bytes = uuri_serialized_s.encode()
            self.__save_serializer_translation(sdk, uuri_serialized)
            
        elif "action" in json_msg and json_msg["action"] == MICRO_URI_DESERIALIZE_RESPONSE:
            # uuri_base64: str = json_msg["message"]
            # protobuf_serialized_data: bytes = base64_to_protobuf_bytes(uuri_base64) 
            # uuri: UUri = RpcMapper.unpack_payload(Any(value=protobuf_serialized_data), UUri)
            # self.__save_serializer_translation(sdk, uuri)
            pass
        else:
            raise Exception("new client connection didn't initally send sdk name")
        
    def __save_status(self, sdk_name: str, status: UStatus):
        ## NOTE: NEED SEMAPHORE for each sdk so dont overwrite a status
        self.sdk_to_received_ustatus_lock.acquire()
        self.sdk_to_received_ustatus[sdk_name] = status 
        self.sdk_to_received_ustatus_lock.release()
    
    def __pop_status(self, sdk_name: str) -> UStatus:
        # blocking: wait till received ustatus
        while self.sdk_to_received_ustatus[sdk_name] is None:
            continue
            
        self.sdk_to_received_ustatus_lock.acquire()
        status: UStatus = self.sdk_to_received_ustatus.pop(sdk_name)
        self.sdk_to_received_ustatus_lock.release()
        
        return status
    
    def __save_serializer_translation(self, sdk_name: str, translation: Union[str, Any]):
        self.sdk_to_serializer_translation_lock.acquire()
        self.sdk_to_serializer_translation[sdk_name] = translation
        self.sdk_to_serializer_translation_lock.release()  
    
    def __pop_serializer_translation(self, sdk_name: str) -> Union[str, Any]:
        while self.sdk_to_serializer_translation[sdk_name] is None:
            continue
            
        self.sdk_to_serializer_translation_lock.acquire()
        serializer_translation: Union[str, Any] = self.sdk_to_serializer_translation.pop(sdk_name)
        self.sdk_to_serializer_translation_lock.release()
        
        return serializer_translation      
    
    def has_sdk_connection(self, sdk_name: str) -> bool:
        if sdk_name == "self":
            return True
        return sdk_name in self.sdk_to_test_agent_socket
        
    def listen_for_client_connections(self):
        """
        Listens for Test Agent Connections and creates a thread to start the init process
        """
        
        while True:
            # Wait until some registered file objects or sockets become ready, or the timeout expires.
            events = self.selector.select()
            for key, mask in events:
                callback = key.data
                callback(key.fileobj)

    @multimethod
    def _send_to_test_agent(self, test_agent_socket: socket.socket, json_message: Dict[str, str]):

        json_message_str: str = convert_json_to_jsonstring(json_message) 
        
        message: bytes = convert_str_to_bytes(json_message_str) 

        send_socket_data(test_agent_socket, message)
        
    @multimethod
    def _send_to_test_agent(self, test_agent_socket: socket.socket, command: str, umsg: UMessage):
        """ Contains data preprocessing and sending UMessage steps to Test Agent

        Args:
            test_agent_socket (socket.socket): Test Agent Socket
            command (str): message's action-type
            umsg (UMessage): the raw protobuf message 
        """
        json_message = {
            "action": command,
            "message": protobuf_to_base64(umsg) 
        }

        self._send_to_test_agent(test_agent_socket, json_message)
    
    @multimethod
    def _send_to_test_agent(self, test_agent_socket: socket.socket, command: str, uri: UUri):
        """ For uri serializer (serialize/deserialize) mostly
        """
        json_message = {
            "action": command,
            "message": protobuf_to_base64(uri) 
        }
        self._send_to_test_agent(test_agent_socket, json_message)
    
    @multimethod
    def _send_to_test_agent(self, test_agent_socket: socket.socket, command: str, protobuf_serialized: str):
        """ For uri serializer (serialize/deserialize) mostly
        """
        json_message = {
            "action": command,
            "message": protobuf_serialized
        }
        self._send_to_test_agent(test_agent_socket, json_message)
    
    @multimethod
    def _send_to_test_agent(self, test_agent_socket: socket.socket, command: str, protobuf_serialized: bytearray):
        """ For uri serializer (serialize/deserialize) mostly
        """
        json_message = {
            "action": command,
            "message": protobuf_serialized.decode()
        }
        self._send_to_test_agent(test_agent_socket, json_message)
        
    def request(self, sdk_ta_destination: str, command: str, message: UMessage) -> UStatus:
        """Sends different requests to a specific SDK Test Agent

        Args:
            sdk_ta_destination (str): SDK Test Agent
            command (str): send, registerlistener, unregisterlistener, invokemethod
            message (UMessage): message data to send to the SDK Test Agent

        Returns:
            UStatus: response Status
        """
        sdk_ta_destination = sdk_ta_destination.lower().strip()

        test_agent_socket: socket.socket = self.sdk_to_test_agent_socket[sdk_ta_destination]

        self._send_to_test_agent(test_agent_socket, command, message)
        
        status: UStatus = self.__pop_status(sdk_ta_destination) 
        return status


    def get_or_null(self, json_request: Dict, json_key: str):
        return json_request.get(json_key, [None])[0]

    def json_action_request(self, json_request: Dict) -> UStatus:
        """Runtime command to send to Test Agent based on request json

        Args:
            json_request (Dict): the command that needs to run but formatted in a json
            listener (UListener): required listener if need to run registerListener()

        Returns:
            UStatus: the status after doing a command
        """
        
        ## NOTE: in tck impl, need to assert UStatus's code, NOT MESSAGE
    

        sdk_name: str = self.get_or_null(json_request, "ue")
        command: str = self.get_or_null(json_request, "action")

        uri_authority_name: str = self.get_or_null(json_request, "uri.authority.name")

        if self.get_or_null(json_request, "uri.authority.ip") is not None and \
            self.get_or_null(json_request, "uri.authority.id") is not None:
            raise ValueError("Cannot set both uri.authority.ip and uri.authority.id")
        
        uri_authority_name: str = self.get_or_null(json_request, "uri.authority.name")

        if self.get_or_null(json_request, "uri.authority.ip") is not None:
            # .encode() isnt working
            uri_authority_ip: bytes = self.get_or_null(json_request, "uri.authority.ip").encode()
        else:
            uri_authority_ip: bytes = None

        if self.get_or_null(json_request, "uri.authority.id") is not None:
            uri_authority_id: bytes = self.get_or_null(json_request, "uri.authority.id").encode()
        else:
            uri_authority_id: bytes = None

        uri_entity_name: str = self.get_or_null(json_request, "uri.entity.name")

        if self.get_or_null(json_request, "uri.entity.id") is not None:
            uri_entity_id: int = int(self.get_or_null(json_request, "uri.entity.id"))
        else:
            uri_entity_id: int = None

        if self.get_or_null(json_request, "uri.entity.version_major") is not None:
            uri_entity_version_major: int = int(self.get_or_null(json_request, "uri.entity.version_major"))
        else:
            uri_entity_version_major: int = None

        if self.get_or_null(json_request, "uri.entity.version_minor") is not None:
            uri_entity_version_minor: int = int(self.get_or_null(json_request, "uri.entity.version_minor"))
        else:
            uri_entity_version_minor: int = None

        uri_resource_name: str = self.get_or_null(json_request, "uri.resource.name")
        uri_resource_instance: str = self.get_or_null(json_request, "uri.resource.instance")
        uri_resource_message: str = self.get_or_null(json_request, "uri.resource.message")
        if self.get_or_null(json_request, "uri.resource.id") is not None:
            uri_resource_id: int = int(self.get_or_null(json_request, "uri.resource.id"))
        else:
            uri_resource_id: int = None
        sdk_name: str = json_request["ue"][0]
        command: str = json_request["action"][0].lower().strip()
        
        entity: UEntity = UEntityBuilder().add_id(uri_entity_id).add_name(uri_entity_name).add_version_major(uri_entity_version_major).add_version_minor(uri_entity_version_minor).build()
        resource: UResource = UResourceBuilder().add_id(uri_resource_id).add_instance(uri_resource_instance).add_message(uri_resource_message).add_name(uri_resource_name).build()
        authority: UAuthority = UAuthorityBuilder().add_id(uri_authority_id).add_ip(uri_authority_ip).add_name(uri_authority_name).build()
        
        source = UUriBuilder().add_authority(authority).add_entity(entity).add_resource(resource).build()
        
        if command in [SEND_COMMAND, INVOKE_METHOD_COMMAND]:
            format: str = json_request['payload.format'][0]
            format = format.lower()
            if format == "cloudevent":
                values: Dict = json_request["payload.value"]
                id: str = values["id"][0]
                source: str = values["source"][0]

                cloudevent = CloudEvent(spec_version="1.0", source=source, id=id)
                any_obj = Any()
                any_obj.Pack(cloudevent)
                proto: bytes = any_obj.SerializeToString()

            elif format == "protobuf":
                proto: str = json_request["payload.value"][0]
                proto: bytes = proto.encode()
            else:
                raise Exception("payload.format's provided value not handleable")

            upayload: UPayload = UPayload(format=UPayloadFormat.UPAYLOAD_FORMAT_PROTOBUF, value=proto)


            priority: str = self.get_or_null(json_request, "attributes.priority")
            priority: UPriority = get_priority(priority)

            umsg_type: str = self.get_or_null(json_request, "attributes.type")
            umsg_type: UMessageType = get_umessage_type(umsg_type)

            if 'attributes.id' in json_request:
                id_num: int = int(self.get_or_null(json_request, 'attributes.id'))
                id: UUID = UUID(msb=id_num)

            sink: UUri = UUri()
            if "attributes.sink" in json_request:
                sink: str = self.get_or_null(json_request)
                sink_bytes: bytes = sink.encode()
                #sink.ParseFromString(sink_bytes)

            attributes: UAttributes = UAttributesBuilder(id, umsg_type, priority).withSink(sink).build()
            # return self.send_command(sdk_name, command, topic, upayload, attributes)

            if source is not None:
                attributes.source.CopyFrom(source)

            umsg: UMessage = UMessage(attributes=attributes, payload=upayload)
            return self.request(sdk_name, command, umsg)

        elif command in [REGISTER_LISTENER_COMMAND, UNREGISTER_LISTENER_COMMAND]:
            umsg: UMessage = UMessage(attributes=UAttributes(source=source))
            # return self.register_listener_command(sdk_name, command, topic, listener)
            return self.request(sdk_name, command, umsg)
        
        # Serialize and Deserialize
        elif command == LONG_URI_SERIALIZE:
            # Input UUri proto and  TA should respond with str
            # topic = LongUriSerializer().deserialize(uri)
            # topic:str = uri
            print("Sending", source)
            # translation: str = self.raw_protobuf_request(sdk_name, source)
            translation: str = self.uriserializer_request(sdk_name, command, source)

            return translation
        elif command == LONG_URI_DESERIALIZE:
            # Input String and TA should respond with UUri proto
            
            topic_str: str = LongUriSerializer().deserialize(source)
            translation: UUri = self.uriserializer_request(sdk_name, command, topic_str)
            return translation
        elif command == MICRO_URI_SERIALIZE:
            # in: UUri -> out: bytes
            translation: bytes = self.uriserializer_request(sdk_name, command, source)
            return translation
        elif command == MICRO_URI_DESERIALIZE:
            # in: bytes -> out: UUri
            topic_b: bytes = MicroUriSerializer().deserialize(source)
            print("topic_b:", topic_b)
            translation: UUri = self.uriserializer_request(sdk_name, command, topic_b)
            return translation
        else:
            raise Exception("action value not handled!")   

    def uriserializer_request(self, sdk_ta_destination: str, command: str, proto: Union[Any, str, bytearray]) -> Union[Any, str, bytes] :
        """Sends raw data without any JSON wrapped around or any pre-formats
        
        Args:
            sdk_ta_destination (str): _description_
            proto (Union[Any, str]): (ex: UUri proto / string)
        """
        
        sdk_ta_destination = sdk_ta_destination.lower().strip()

        test_agent_socket: socket.socket = self.sdk_to_test_agent_socket[sdk_ta_destination]
        print("proto:", proto)
        print(type(proto))
        self._send_to_test_agent(test_agent_socket, command, proto)
        
        translation: str = self.__pop_serializer_translation(sdk_ta_destination)
        
        return translation
        
    def close(self):
        """Close the selector / test manager's server, 
        BUT need to free its individual SDK TA connections using self.close_ta(sdk) first
        """
        self.selector.close()
    
    def close_ta_socket(self, sdk_name: str):
        logger.info(f"Closing {sdk_name} connection")
        
        # if havent deleted and closed socket client already...
        if sdk_name in self.sdk_to_test_agent_socket:
        
            self.sdk_to_test_agent_socket_lock.acquire()
            ta_socket: socket.socket = self.sdk_to_test_agent_socket[sdk_name]
            
            del self.sdk_to_test_agent_socket[sdk_name]
            self.sdk_to_test_agent_socket_lock.release()

            # Stop monitoring socket/fileobj. A file object shall be unregistered prior to being closed.
            self.selector.unregister(ta_socket)
            ta_socket.close()