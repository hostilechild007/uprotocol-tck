# -------------------------------------------------------------------------
#
# Copyright (c) 2023 General Motors GTO LLC
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
# SPDX-FileCopyrightText: 2023 General Motors GTO LLC
# SPDX-License-Identifier: Apache-2.0
#
# -------------------------------------------------------------------------

import json
import uuid
from typing import List

from google.protobuf.any_pb2 import Any
from uprotocol.proto.uuid_pb2 import UUID
from up_client_socket_python.utils.socket_message_processing_utils import protobuf_to_base64
from test_request.utils.request_utils import ReqIDUtils, ReqCodeRPC


class RPCReqItem:
    """
    Represents an item in an RPC request.

    Attributes:
        method_uri (str): The URI of the RPC method.
        arguments (Any): The arguments to be passed to the RPC method.
        subscribe_to (List[str]): List of topics to be subscribed for listening update.
        timeout (int): Timeout value for the RPC request in milliseconds.
    """

    def __init__(self, method_uri: str = '', arguments: Any = None, subscribe_to: List[str] = None, timeout: int = 0):
        """
        Initialize an RPCReqItem instance.

        Parameters:
            method_uri (str): The URI of the RPC method.
            arguments (Any): The arguments to be passed to the RPC method.
            subscribe_to (List[str]): List of topics to be subscribed for listening update.
            timeout (int): Timeout value for the RPC request in milliseconds.
        """
        self.timeout = timeout
        self.subscribe_to = subscribe_to
        self.arguments = arguments
        self.method_uri = method_uri

    def _to_json_string(self) -> str:
        """
        Convert the RPCReqItem instance to a JSON-formatted string.
        Returns: str: JSON-formatted string representing the RPCReqItem.
        """
        json_dict = self.__dict__
        if 'arguments' in json_dict:
            json_dict['arguments'] = protobuf_to_base64(json_dict['arguments'])
        return json.dumps(json_dict)


class RPCReqList(RPCReqItem):
    """
    Represents a list of RPCReqItem instances.

    Attributes: rpc_req_items (List[str]): List of JSON-formatted strings representing RPCReqItem instances.
    """

    def __init__(self):
        """
        Initialize an RPCReqList instance.
        """
        super().__init__()
        self.rpc_req_items = []

    def add_rpc_item(self, rpc_item: RPCReqItem = None):
        """
        Add an RPCReqItem to the RPCReqList.
        Parameters: rpc_item (RPCReqItem): The RPCReqItem to be added.
        Returns: RPCReqList: The updated RPCReqList instance.
        """
        if RPCReqItem:
            self.rpc_req_items.append(rpc_item._to_json_string())
        return self

    def get_rpc_req_items(self) -> [str]:
        """
        Get the list of JSON-formatted strings representing RPCReqItem instances.
        Returns: List[str]: List of JSON-formatted strings.
        """
        return self.rpc_req_items

    def __str__(self):
        """
        Return a string representation of the RPCReqList.
        Returns: str: String representation of the RPCReqList.
        """
        return str(self.rpc_req_items)


class RPCRequest:
    """
    Represents an RPC request.

    Attributes:
        id (uuid.UUID): The unique identifier for the request. If not provided, a new UUIDv4 is generated.
        code (str): The code associated with the RPCRequest.
        rpc_list (List[RPCReqItem]): List of RPCReqItem instances.
        rpc_interval (int): The interval associated with the request in milliseconds.
        thread_count (int): The thread count associated with the request.
        cycles (int): The number of cycles associated with the request.
        definite_interval (bool): Indicates whether the interval is definite or not.
    """

    def __init__(self, code: str = '', rpc_list: List[RPCReqItem] = None, rpc_interval: int = 0,
                 definite_interval: bool = False, thread_count: int = 0,
                 cycles: int = 0, id: uuid.UUID = None):
        """
        Initialize an RPCRequest instance.

        Parameters:
            code (str): The code associated with the request.
            rpc_list (List[RPCReqItem]): List of RPCReqItem instances.
            rpc_interval (int): The interval associated with the request in milliseconds.
            definite_interval (bool): Indicates whether the interval is definite or not.
            thread_count (int): The thread count associated with the request.
            cycles (int): The number of cycles associated with the request.
            id (uuid.UUID): The unique identifier for the request. If not provided, a new UUIDv4 is generated.
        """
        self.id = id or ReqIDUtils.generate_request_id()
        self.code = code
        self.rpc_list = rpc_list
        self.rpc_interval = rpc_interval
        self.thread_count = thread_count
        self.cycles = cycles
        self.definite_interval = definite_interval

    def to_json_string(self) -> str:
        """
        Convert the RPCRequest instance to a JSON-formatted string.
        Returns: str: JSON-formatted string representing the RPCRequest.
        """
        json_dict = self.__dict__.copy()
        json_dict['rpc-list'] = json_dict.pop('rpc_list')
        json_dict['definite-interval'] = json_dict.pop('definite_interval')
        json_dict['thread-count'] = json_dict.pop('thread_count')
        if 'id' in json_dict:
            json_dict['id'] = str(json_dict['id'])
        return json.dumps(json_dict)


if __name__ == "__main__":
    # Example usage:

    # set proto UUID sample, later change to appropriate proto message class based on method uri
    arg1 = UUID(msb=1234, lsb=5678)
    arg2 = UUID(msb=123, lsb=5678)

    # Create RPCReqItem instances
    rpc_req_item1 = RPCReqItem(method_uri='body.cabin_climate//rpc.ClimateCommand', arguments=arg1,
                               subscribe_to=["/body.access//door.front_left#Door"],
                               timeout=3000)
    rpc_req_item2 = RPCReqItem(method_uri='body.cabin_climate//rpc.ClimateCommand', arguments=arg2,
                               subscribe_to=["/body.access//door.front_right#Door"],
                               timeout=3000)

    # Create RPCReqList and add RPCReqItem instances
    rpc_req_list = RPCReqList()
    rpc_req_list.add_rpc_item(rpc_req_item1).add_rpc_item(rpc_req_item2)

    # Create RPCRequest with the RPCList and other parameters
    rpc_request_json_string = RPCRequest(code=ReqCodeRPC.CMD_RPC, rpc_list=rpc_req_list.get_rpc_req_items(),
                                         rpc_interval=5000,
                                         definite_interval=True, thread_count=1, cycles=10).to_json_string()

    # Print the created RPCRequest json formatted string
    print(rpc_request_json_string)
