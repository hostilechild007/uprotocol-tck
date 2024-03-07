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

Feature: Test Manager and Test Agent messaging to each other directly or with SocketUTransport and Dispatcher

#NOTE: A behavior scenario specification should focus on one individual behavior

    Scenario Outline: Test Manager's registerlistener() request to Test Agent
        #New Given: set data first for (UUri, UPayload, UAttributes)
        # should have separate scenarios checking status for registerlistener() and send()

        # Note: each step should be DESCRIPTIVE as POSSIBLE!
        Given protobuf UEntity "entity" sets parameter "name" equal to string "body.access"  
            And protobuf UResource "resource" sets parameter "name" equal to string "door" 
            And protobuf UResource "resource" sets parameter "instance" equal to string "front_left" 
            And protobuf UResource "resource" sets parameter "message" equal to string "Door" 

            And protobuf UUri "uuri" sets parameter "entity" equal to created protobuf "entity"
            And protobuf UUri "uuri" sets parameter "resource" equal to created protobuf "resource"
        
        When Test Manager sends "registerlistener" request to Test Agent "<uE1>"
        Then Test Manager receives an "OK" status for "registerlistener" request

        Examples: 
        | uE1     |
        | python  |
        | java    |

    Scenario Outline: Testing Test Manager's send() request to Test Agent

        Given protobuf UEntity "entity" sets parameter "name" equal to string "body.access"  
            And protobuf UResource "resource" sets parameter "name" equal to string "door" 
            And protobuf UResource "resource" sets parameter "instance" equal to string "front_left" 
            And protobuf UResource "resource" sets parameter "message" equal to string "Door" 
            And protobuf UUri "uuri" sets parameter "entity" equal to created protobuf "entity"
            And protobuf UUri "uuri" sets parameter "resource" equal to created protobuf "resource"

            And protobuf UAttributes "uattributes" creates publish message with parameter source equal to created protobuf "uuri"

            And protobuf UPayload "payload" sets parameter "format" equal to "UPAYLOAD_FORMAT_PROTOBUF"
            And protobuf UPayload "payload" sets parameter "value" equal to "serialized protobuf data"
        
        When Test Manager sends "send" request to Test Agent "<uE1>"
        Then Test Manager receives an "OK" status for "send" request


        Examples: 
        | uE1     |
        | python  |
        | java    |


    Scenario Outline: Testing if registered Test Agent listener will receive sent message via SocketUTransport

        Given protobuf UEntity "entity" sets parameter "name" equal to string "body.access"  
            And protobuf UResource "resource" sets parameter "name" equal to string "door" 
            And protobuf UResource "resource" sets parameter "instance" equal to string "front_left" 
            And protobuf UResource "resource" sets parameter "message" equal to string "Door" 
            And protobuf UUri "uuri" sets parameter "entity" equal to created protobuf "entity"
            And protobuf UUri "uuri" sets parameter "resource" equal to created protobuf "resource"

            And protobuf UAttributes "uattributes" creates publish message with parameter source equal to created protobuf "uuri"

            And protobuf UPayload "payload" sets parameter "format" equal to "UPAYLOAD_FORMAT_PROTOBUF"
            And protobuf UPayload "payload" sets parameter "value" equal to "serialized protobuf data"
        
        When Test Manager sends "registerlistener" request to Test Agent "<uE1>"
            And Test Manager sends "send" request to Test Agent "<uE2>"

        Then Test Manager receives OnReceive UMessage from "<uE1>" Test Agent with parameter UPayload "payload" with parameter "value" as "serialized protobuf data"


        Examples: Test Agents
        | uE1     | uE2    |
        | python  | java   |
        | python  | python |
        | java    | python |
