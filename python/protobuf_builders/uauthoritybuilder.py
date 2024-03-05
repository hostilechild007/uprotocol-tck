# -------------------------------------------------------------------------
#
# Copyright (c) 2024 General Motors GTO LLC
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for setitional information
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

from uprotocol.proto.uri_pb2 import UAuthority

from protobuf_builders.builder import Builder

NAME_VAR: str = "name"
ID_VAR: str = "id"
IP_VAR: str = "ip"

class UAuthorityBuilder(Builder):

    def __init__(self):
        self.ip: bytes = None
        self.id: bytes = None
        self.name: str = None
    
    def set_ip(self, ip : bytes):
        
        self.ip = ip
        self.id = None

        return self
    
    def set_id(self, id: bytes):
        self.id = id
        self.ip = None

        return self

    def set_name(self, name : str):
        
        self.name = name
        return self
    
    def set(self, attribute_name: str, attribute_value: str):
        attribute_name = attribute_name.lower().strip()
        
        if attribute_name == NAME_VAR:
            return self.set_name(attribute_value)
        elif attribute_name == ID_VAR:
            return self.set_id(attribute_value.encode())
        elif attribute_name == IP_VAR:
            return self.set_ip(attribute_value.encode())
        else:
            raise ValueError(f"{self.__class__.__name__} doesn't handle attribute name {attribute_name}")

    def build(self) -> UAuthority:
        """

        @return Returns a constructed
        """
        attributes = UAuthority()
            
        if self.ip is not None:
            attributes.ip = self.ip
        if self.id is not None:
            attributes.id = self.id
        if self.name is not None:
            attributes.name = self.name
        return attributes

# authority = UAuthorityBuilder().set_ip(b"4321").set_id(b"1234").set_id(b"1234").set_ip(b"4321").set_name("name").build()
# print("authority.name:", authority.name)
# print(authority.ip)
# print(authority.id)
# print("authority: ", authority)
authority = UAuthorityBuilder().set("ip", "4321").set("ip", "1234").set("id", "1234").set("name", "name").build()
print(authority)