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

Feature: Test Agents testing messaging to each other and internal UTransport with send, registerlistener, and invokemethod

#NOTE: A behavior scenario specification should focus on one individual behavior
    
    Scenario Outline: To test the registerlistener and send apis
        Given “<uE1>” creates data for "registerlistener"
            And sets "uri.entity.name" to "body.access"
            And sets "uri.resource.name" to "door"
            And sets "uri.resource.instance" to "front_left"
            And sets "uri.resource.message" to "Door"
            And sends "registerlistener" request
            And the status for "registerlistener" request is "OK"

        When “<uE2>” creates data for "send"
            And sets "uri.entity.name" to "body.access"
            And sets "uri.resource.name" to "door"
            And sets "uri.resource.instance" to "front_left"
            And sets "uri.resource.message" to "Door"
            And sets "attributes.priority" to "UPRIORITY_CS1"
            And sets "attributes.type" to "UMESSAGE_TYPE_PUBLISH"
            And sets "attributes.id" to "12345"
            And sets "payload.format" to "protobuf"
            And sets "payload.value" to "serialized protobuf data"
            And sends "send" request
            And the status for "send" request is "OK"

        Then "<uE1>" receives "payload.value" as "serialized protobuf data"

        Examples: topic_names
        | uE1     | uE2    |
        | python  | java   |
        | python  | python |
        | java    | python |
    
    
    Scenario Outline: Test Agent's registerlistener() on given UUri
        #New Given: set data first for (UUri, UPayload, UAttributes)
        # should have separate scenarios checking status for registerlistener() and send()

        # Note: each step should be DESCRIPTIVE as POSSIBLE!
        Given Test Agent sets UEntity "entity" field "name" equal to string "body.access"  
            And Test Agent sets UResource "resource" field "name" equal to string "door" 
            And Test Agent sets UResource "resource" field "instance" equal to string "front_left" 
            And Test Agent sets UResource "resource" field "message" equal to string "Door" 

            And Test Agent sets UUri "uuri" field "entity" equal to created protobuf "entity"
            And Test Agent sets UUri "uuri" field "resource" equal to created protobuf "resource"
            
        
        When Test Agent "<uE1>" executes "registerlistener" on given UUri
        Then Test Agent "<uE1>" receives an "OK" status for latest execute

        Examples: 
        | uE1     |
        | python  |
        | java    |

    Scenario Outline: Testing Test Manager's send() on given UUri

        Given Test Agent sets UEntity "entity" field "name" equal to string "body.access"  
            And Test Agent sets UResource "resource" field "name" equal to string "door" 
            And Test Agent sets UResource "resource" field "instance" equal to string "front_left" 
            And Test Agent sets UResource "resource" field "message" equal to string "Door" 
            And Test Agent sets UUri "uuri" field "entity" equal to created protobuf "entity"
            And Test Agent sets UUri "uuri" field "resource" equal to created protobuf "resource"

            And Test Agent sets UAttributes "uattributes" creates publish message with parameter source equal to created protobuf "uuri"

            And Test Agent sets UPayload "payload" field "format" equal to "UPAYLOAD_FORMAT_PROTOBUF"
            And Test Agent sets UPayload "payload" field "value" equal to "serialized protobuf data"
        
        When Test Agent "<uE1>" executes "send" on given UUri
        Then Test Agent "<uE1>" receives an "OK" status for latest execute


        Examples: 
        | uE1     |
        | python  |
        | java    |


    Scenario Outline: Testing if registered Test Agent listener will receive sent message via SocketUTransport

        Given Test Agent sets UEntity "entity" field "name" equal to string "body.access"  
            And Test Agent sets UResource "resource" field "name" equal to string "door" 
            And Test Agent sets UResource "resource" field "instance" equal to string "front_left" 
            And Test Agent sets UResource "resource" field "message" equal to string "Door" 
            And Test Agent sets UUri "uuri" field "entity" equal to created protobuf "entity"
            And Test Agent sets UUri "uuri" field "resource" equal to created protobuf "resource"

            And Test Agent sets UAttributes "uattributes" creates publish message with parameter source equal to created protobuf "uuri"

            And Test Agent sets UPayload "payload" field "format" equal to "UPAYLOAD_FORMAT_PROTOBUF"
            And Test Agent sets UPayload "payload" field "value" equal to "serialized protobuf data"
        
        When Test Agent "<uE1>" executes "registerlistener" on given UUri
            And Test Agent "<uE2>" executes "send" on given UUri

        Then Test Agent "<uE1>" builds OnReceive UMessage with parameter UPayload "payload" with parameter "value" as "serialized protobuf data"


        Examples: Test Agents
        | uE1     | uE2    |
        | python  | java   |
        | python  | python |
        | java    | python |

    Scenario Outline: Testing Test Manager's invoke_method() request sent to Test Agent

        Given Test Agent sets UEntity "entity" field "name" equal to string "body.access"  
            And Test Agent sets UResource "resource" field "name" equal to string "door" 
            And Test Agent sets UResource "resource" field "instance" equal to string "front_left" 
            And Test Agent sets UResource "resource" field "message" equal to string "Door" 
            And Test Agent sets UUri "uuri" field "entity" equal to created protobuf "entity"
            And Test Agent sets UUri "uuri" field "resource" equal to created protobuf "resource"

            And Test Agent sets UAttributes "uattributes" creates publish message with parameter source equal to created protobuf "uuri"

            And Test Agent sets UPayload "payload" field "format" equal to "UPAYLOAD_FORMAT_PROTOBUF"
            And Test Agent sets UPayload "payload" field "value" equal to "serialized protobuf data"
        
        When Test Agent "<uE1>" executes "invokemethod" on given UUri

        Then Test Agent "<uE1>" receives an "OK" status for latest execute

        Examples: 
        | uE1     |
        | python  |
        | java    |

    Scenario Outline: Testing Test Agent's invoke_method() subscribes to the responded UMessage topic

        Given Test Agent sets UEntity "entity" field "name" equal to string "body.access"  
            And Test Agent sets UResource "resource" field "name" equal to string "door" 
            And Test Agent sets UResource "resource" field "instance" equal to string "front_left" 
            And Test Agent sets UResource "resource" field "message" equal to string "Door" 
            And Test Agent sets UUri "uuri" field "entity" equal to created protobuf "entity"
            And Test Agent sets UUri "uuri" field "resource" equal to created protobuf "resource"

            And Test Agent sets UAttributes "uattributes" creates publish message with parameter source equal to created protobuf "uuri"

            And Test Agent sets UPayload "payload" field "format" equal to "UPAYLOAD_FORMAT_PROTOBUF"
            And Test Agent sets UPayload "payload" field "value" equal to "serialized protobuf data"

        When Test Agent "<uE1>" executes "registerlistener" on given UUri
            And Test Agent "<uE2>" executes "invokemethod" on given UUri
            And Test Agent "<uE2>" executes "unregisterlistener" on given UUri

        # NEW way of commenting without mentioning "Test manager": ...
        # Given protobuf UEntity "entity" sets field "name" equal to string "body.access"  
        # When Test Agent "<uE1>" executes "registerlistener" on given UUri 
        #     And Test Agent "<uE2>" executes "invokemethod" on given UUri 
        Then Test Agent "<uE2>" receives an "OK" status for latest execute

        Examples: Test Agents
        | uE1     | uE2    |
        | python  | python |
    # Scenario Outline: Testing Test Manager's long uri serializer on given UUri

    #     Given protobuf UEntity "entity" field "name" equal to string "body.access"  
    #         And protobuf UResource "resource" field "name" equal to string "door" 
    #         And protobuf UResource "resource" field "instance" equal to string "front_left" 
    #         And protobuf UResource "resource" field "message" equal to string "Door" 
    #         And protobuf UUri "uuri" field "entity" equal to created protobuf "entity"
    #         And protobuf UUri "uuri" field "resource" equal to created protobuf "resource"
        
    #     When Test Agent "<uE1>" executes "longuriserialize" uri serializer on given UUri "<uE1>"

    #     Then Test Manager receives a string "/body.access//door.front_left#Door"

    #     Examples: 
    #     | uE1     |
    #     | python  |
    

    # Scenario Outline: Testing Test Manager's long uri deserializer on given UUri

    #     Given serialized UUri string "/body.access//door.front_left#Door"
        
    #     When Test Agent "<uE1>" executes "longurideserialize" uri serializer on given UUri "<uE1>"

    #     Then Test Manager receives a protobuf UUri "/body.access//door.front_left#Door"

    #     Examples: 
    #     | uE1     |
    #     | python  |
