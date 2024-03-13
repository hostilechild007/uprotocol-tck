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

from uprotocol.proto.umessage_pb2 import UMessage
from uprotocol.proto.uri_pb2 import UUri
from uprotocol.proto.upayload_pb2 import UPayload
from uprotocol.proto.uattributes_pb2 import UAttributes


SOURCE_VAR: str = "source"
PAYLOAD_VAR: str = "payload"
ATTRIBUTES_VAR: str = "attribute"

class UMessageGetter:
    def __init__(self, umsg: UMessage) -> None:        
        self.umsg: UMessage = umsg
        
    def get_source(self) -> UUri:
        return self.umsg.attributes.source
    
    def get_payload(self) -> UPayload:
        return self.umsg.payload
    
    def get_attributes(self) -> UAttributes:
        return self.umsg.attributes
    
    def get(self, param_name: str):
        param_name = param_name.lower().strip()
        
        if param_name == SOURCE_VAR:
            return self.get_source()
        elif param_name == PAYLOAD_VAR:
            return self.get_payload()
        elif param_name == ATTRIBUTES_VAR:
            return self.get_attributes()
        else:
            raise ValueError(f"{self.__class__.__name__} doesn't have param {param_name}")