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

Feature: Protobuf Builder/Factory Testing

  Scenario Outline: To test the UAttributes Builder
    Given Test Agent "<uE1>" begins "<Builder>" test
        And sets "uattributes.source.entity.name" to "body.access"
        And sets "uattributes.source.resource.name" to "door"
        And sets "uattributes.source.resource.instance" to "front_left"
        And sets "uattributes.source.resource.message" to "Door"
    
    When Test Agent "<uE1>" executes "<Builder>" on given protobuf
    # Then Test Agent "<uE1>" receives "/body.access//door.front_left#Door"

    # data -> <transfer> -> TM -> <send> -> TA (deserialize/sserialize) -> <send> -> TM -> <take response and send> -> UE2/3 (do opposite of serialization) -> <send response> -> TM
    # End: assert(original send vs. final response)
    # BUilders will be very similar to SErializers, but only send (ex: str) and response (ex: UURI) 

    # validator: uuri or string -> <send> -> TA (deserialize/serialze) -> <send response> -> TM use response and ask TA to validate -> <send> -> TA validates -> <send response> -> TM gets bool and message

    Examples:

    |    uE1    |     Builder          |
    |   python  |     uattributesbuilder    |