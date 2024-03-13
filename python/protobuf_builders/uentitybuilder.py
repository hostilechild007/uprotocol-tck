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


from uprotocol.proto.uri_pb2 import UEntity 
from protobuf_builders.builder import Builder


NAME_VAR: str = "name"
ID_VAR: str = "id"
VERSION_MAJOR_VAR: str = "version_major"
VERSION_MINOR_VAR: str = "version_minor"

class UEntityBuilder(Builder):
    def __init__(self) -> None:
        self.name: str = None
        self.id: int = None
        self.version_major: int = None
        self.version_minor: int = None
    
    def set_name(self, name: str):
        
        self.name = name
        return self
    
    def set_id(self, id : int):
        self.id = id

        return self
    
    def set_version_major(self, version_major: int):

        self.version_major = version_major

        return self
    
    def set_version_minor(self, version_minor : int):

        self.version_minor = version_minor 

        return self
    
    def set(self, attribute_name: str, attribute_value: str):
        attribute_name = attribute_name.lower().strip()
        
        if attribute_name == NAME_VAR:
            return self.set_name(attribute_value)
        elif attribute_name == ID_VAR:
            return self.set_id(int(attribute_value))
        elif attribute_name == VERSION_MAJOR_VAR:
            return self.set_version_major(int(attribute_value))
        elif attribute_name == VERSION_MINOR_VAR:
            return self.set_version_minor(int(attribute_value))
        else:
            raise ValueError(f"{self.__class__.__name__} doesn't handle attribute name {attribute_name}")
    
    def build(self) -> UEntity:
        """

        @return Returns a constructed
        """
        proto = UEntity()
            
        if self.name is not None:
            proto.name = self.name
        if self.id is not None:
            proto.id = self.id
        if self.version_major is not None:
            proto.version_major = self.version_major
        if self.version_minor is not None:
            proto.version_minor = self.version_minor
        return proto
    