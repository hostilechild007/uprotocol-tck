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


from protobuf_builders.builder import Builder
from uprotocol.proto.umessage_pb2 import UMessage
from uprotocol.proto.uattributes_pb2 import UAttributes
from uprotocol.proto.uri_pb2 import UUri
from uprotocol.proto.upayload_pb2 import UPayload

class UMessageBuilder(Builder):
    def __init__(self) -> None:
        self.attributes: UAttributes = None
        self.payload: UPayload = None
        self.uuri: UUri = None
        
    def set_attributes(self, attributes: UAttributes):
        self.attributes = attributes
        return self
    
    def set_payload(self, payload: UPayload):
        self.payload = payload
        return self
    
    def set_uuri(self, uuri: UUri):
        self.uuri = uuri
        return self
    
    def build(self) -> UMessage:
        
        proto = UMessage()
        
        if self.attributes is not None:
            proto.attributes.CopyFrom(self.attributes)            
        if self.payload is not None:
            proto.payload.CopyFrom(self.payload)
        if self.uuri is not None:
            if self.attributes is None:
                proto.attributes.CopyFrom(UAttributes())
            proto.attributes.source.CopyFrom(self.uuri)
            
        return proto