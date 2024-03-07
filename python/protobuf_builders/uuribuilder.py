# -------------------------------------------------------------------------

# Copyright (c) 2023 General Motors GTO LLC
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
# SPDX-FileCopyrightText: 2023 General Motors GTO LLC
# SPDX-License-Identifier: Apache-2.0

# -------------------------------------------------------------------------

from google.protobuf.any_pb2 import Any

from uprotocol.proto.uri_pb2 import UUri, UAuthority, UEntity, UResource
from protobuf_builders.builder import Builder

AUTHORITY_VAR: str = "authority"
ENTITY_VAR: str = "entity"
RESOURCE_VAR: str = "resource"


class UUriBuilder(Builder):

    def __init__(self):
        self.authority: UAuthority = None
        self.entity: UEntity = None
        self.resource: UResource = None
        
    def set_authority(self, authority: UAuthority):
        self.authority = authority
        return self
    
    def set_entity(self, entity: UEntity):
        self.entity = entity
        return self
    
    def set_resource(self, resource: UResource):
        self.resource = resource
        return self
    
    def set(self, attribute_name: str, proto: Any):
        attribute_name = attribute_name.lower().strip()
        
        if attribute_name == AUTHORITY_VAR:
            return self.set_authority(proto)
        elif attribute_name == ENTITY_VAR:
            return self.set_entity(proto)
        elif attribute_name == RESOURCE_VAR:
            return self.set_resource(proto)
        else:
            raise ValueError(f"{self.__class__.__name__} doesn't handle attribute name {attribute_name}")

    def build(self) -> UUri:
        """
        Construct the UAttributes from the builder.

        @return Returns a constructed
        """

        proto = UUri()
            
        if self.authority is not None:
            proto.authority.CopyFrom(self.authority)
        if self.entity is not None:
            proto.entity.CopyFrom(self.entity)
        if self.resource is not None:
            proto.resource.CopyFrom(self.resource)
    
        return proto