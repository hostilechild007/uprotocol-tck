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

Feature: Testing Test Agent's invoke_method() request with respective response

    Scenario Outline: Testing Test Agent's invoke_method() request with respective response
        Given Test Agent "<uE1>" begins "invokemethod" test
            And sets "umessage.attributes.source.entity.name" to "body.access"
            And sets "umessage.attributes.source.resource.name" to "door"
            And sets "umessage.attributes.source.resource.instance" to "front_left"
            And sets "umessage.attributes.source.resource.message" to "Door"

            And sets "umessage.attributes.priority" to "UPRIORITY_CS0"
            And sets "umessage.attributes.type" to "UMESSAGE_TYPE_PUBLISH"
            And sets "umessage.attributes.id.msb" to 123.123

            And sets "umessage.payload.format" to "UPAYLOAD_FORMAT_PROTOBUF"
            And sets "umessage.payload.value" to "serialized protobuf data"

        When Test Agent "<uE1>" executes "invokemethod" on given protobuf

        # Then Test Agent "<uE1>" receives an "OK" status for latest execute

        Examples: 
        | uE1     |
        | python  |
        | java    |

    Scenario Outline: Testing Test Agent's invoke_method() subscribes to the responded UMessage topic

        Given Test Agent "<uE1>" begins "invokemethod" test
            And sets "umessage.attributes.source.entity.name" to "body.access"
            And sets "umessage.attributes.source.resource.name" to "door"
            And sets "umessage.attributes.source.resource.instance" to "front_left"
            And sets "umessage.attributes.source.resource.message" to "Door"

            And sets "umessage.attributes.priority" to "UPRIORITY_CS0"
            And sets "umessage.attributes.type" to "UMESSAGE_TYPE_PUBLISH"
            And sets "umessage.attributes.id.msb" to 123.123

            And sets "umessage.payload.format" to "UPAYLOAD_FORMAT_PROTOBUF"
            And sets "umessage.payload.value" to "serialized protobuf data"

        # When Test Agent "<uE1>" executes "registerlistener" on given UUri
        #     And Test Agent "<uE2>" executes "invokemethod" on given UUri
        #     And Test Agent "<uE1>" executes "unregisterlistener" on given UUri

        # Then Test Agent "<uE2>" receives an "OK" status for latest execute

        Examples: Test Agents
        | uE1     | uE2    |
        | python  | python |
        | python  | java   |
        | java    | python |
        | java    | java   |