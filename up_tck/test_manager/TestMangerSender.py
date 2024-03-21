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
from typing import Dict

from multimethod import multimethod

from uprotocol.proto.uri_pb2 import UUri
from uprotocol.proto.umessage_pb2 import UMessage

from up_tck.python_utils.socket_message_processing_utils import convert_json_to_jsonstring, convert_str_to_bytes, create_json_message, protobuf_to_base64, send_socket_data


class TestManagerSender:
    
    @multimethod
    def send_to_test_agent(self, test_agent_socket: socket.socket, json_message: Dict[str, str]):

        json_message_str: str = convert_json_to_jsonstring(json_message)

        message: bytes = convert_str_to_bytes(json_message_str)

        send_socket_data(test_agent_socket, message)

    @multimethod
    def send_to_test_agent(self, test_agent_socket: socket.socket, command: str, umsg: UMessage):
        """ Contains data preprocessing and sending UMessage steps to Test Agent

        Args:
            test_agent_socket (socket.socket): Test Agent Socket
            command (str): message's action-type
            umsg (UMessage): the raw protobuf message
        """
        json_message = create_json_message(command, protobuf_to_base64(umsg))

        self.send_to_test_agent(test_agent_socket, json_message)

    @multimethod
    def send_to_test_agent(self, test_agent_socket: socket.socket, command: str, uri: UUri):
        """ For uri serializer (serialize/deserialize) mostly
        """
        json_message = create_json_message(command, protobuf_to_base64(uri))
        self.send_to_test_agent(test_agent_socket, json_message)

    @multimethod
    def send_to_test_agent(self, test_agent_socket: socket.socket, command: str, protobuf_serialized: str):
        """ For uri serializer (serialize/deserialize) mostly
        """
        json_message = create_json_message(command, protobuf_serialized)
        self.send_to_test_agent(test_agent_socket, json_message)

    @multimethod
    def send_to_test_agent(self, test_agent_socket: socket.socket, command: str, protobuf_serialized: bytearray):
        """ For uri serializer (serialize/deserialize) mostly
        """
        json_message = create_json_message(command, protobuf_serialized.decode())
        self.send_to_test_agent(test_agent_socket, json_message)