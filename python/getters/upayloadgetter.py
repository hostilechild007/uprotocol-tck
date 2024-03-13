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

from python.up_proto_params_constant.upayload_param_names import REFERENCE_VAR, VALUE_VAR, LENGTH_VAR, FORMAT_VAR


class UPayloadGetter:
    def __init__(self, upayload: UPayload) -> None:
        self.upayload = upayload
    
    def get_reference(self) -> int:
        return self.upayload.reference 
    
    def get_value(self) -> bytes:
        return self.upayload.value
    
    def get_length(self) -> int:
        return self.upayload.length
    
    def get_format(self) -> UPayloadFormat:
        return self.upayload.format 
    
    def get(self, param_name: str):
        
        if param_name == REFERENCE_VAR:
            return self.get_reference()
        elif param_name == VALUE_VAR:
            return self.get_value()
        elif param_name == LENGTH_VAR:
            return self.get_length()
        elif param_name == FORMAT_VAR:
            return self.get_format()
        else:
            raise ValueError(f"{self.__class__.__name__} doesn't handle attribute name {param_name}")