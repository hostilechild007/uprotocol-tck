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
import sys

from uprotocol.proto.upayload_pb2 import UPayload, UPayloadFormat

sys.path.append("../")
from python.protobuf_builders.builder import Builder
from python.utils.proto_format_utils import get_upayload_format
from python.up_proto_params_constant.upayload_param_names import REFERENCE_VAR, VALUE_VAR, LENGTH_VAR, FORMAT_VAR

class UPayloadBuilder(Builder):
    def __init__(self) -> None:
        self.reference: int = None
        self.value: bytes  = None
        self.length: int = None
        self.format: UPayloadFormat = None

    def set_reference(self, reference: int):
        
        self.reference = reference
        self.value = None

        return self
    
    def set_value(self, value: bytes):
        self.reference = None
        self.value = value

        return self
    
    def set_length(self, length: int):
        self.length = length
        return self
    
    def set_format(self, format: UPayloadFormat):
        self.format = format
        return self

    def set(self, attribute_name: str, attribute_value: str):
        attribute_name = attribute_name.lower().strip()
        
        if attribute_name == REFERENCE_VAR:
            return self.set_reference(int(attribute_value))
        elif attribute_name == VALUE_VAR:
            return self.set_value(attribute_value.encode())
        elif attribute_name == LENGTH_VAR:
            return self.set_length(int(attribute_value))
        elif attribute_name == FORMAT_VAR:
            return self.set_format(get_upayload_format(attribute_value))
        else:
            raise ValueError(f"{self.__class__.__name__} doesn't handle attribute name {attribute_name}")
    
    def build(self) -> UPayload:
        proto = UPayload()
            
        if self.reference is not None:
            proto.reference = self.reference
        if self.value is not None:
            proto.value = self.value
        if self.length is not None:
            proto.length = self.length
        if self.format is not None:
            proto.format = self.format
        return proto
