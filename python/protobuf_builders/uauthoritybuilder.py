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

from uprotocol.proto.uri_pb2 import UAuthority


class UAuthorityBuilder:

    def __init__(self):
        self.ip: bytes = None
        self.id: bytes = None
        self.oneof_count = 0
        self.name: str = None
    
    def add_ip(self, ip : bytes):
        
        self.ip = ip
        self.id = None

        return self
    
    def add_id(self, id: bytes):
        self.id = id
        self.ip = None

        return self

    def add_name(self, name : str):
        
        self.name = name
        return self

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

# authority = UAuthorityBuilder().add_ip(b"4321").add_id(b"1234").add_id(b"1234").add_ip(b"4321").add_name("name").build()
# print("authority.name:", authority.name)
# print(authority.ip)
# print(authority.id)
# print("authority: ", authority)