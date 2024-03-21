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

Feature: Serializer and Deserializer Testing

  Scenario Outline: Test the Long URI Serializer
    Given Test Agent "<uE1>" begins "<Serializer>" test
      And sets "uuri.entity.name" to "body.access"
      And sets "uuri.resource.name" to "door"
      And sets "uuri.resource.instance" to "front_left"
      And sets "uuri.resource.message" to "Door"
    
    When Test Agent "<uE1>" executes "<Serializer>" on given protobuf
    # Then Test Agent "<uE1>" receives "/body.access//door.front_left#Door"

    # data -> <transfer> -> TM -> <send> -> TA (deserialize/sserialize) -> <send> -> TM -> <take response and send> -> UE2/3 (do opposite of serialization) -> <send response> -> TM
    # End: assert(original send vs. final response)
    # BUilders will be very similar to SErializers, but only send (ex: str) and response (ex: UURI) 

    # validator: uuri or string -> <send> -> TA (deserialize/serialze) -> <send response> -> TM use response and ask TA to validate -> <send> -> TA validates -> <send response> -> TM gets bool and message

    Examples:

    |    uE1    |     Serializer          |
    |   python  |     longuriserialize    |
    # |   python  |     mircouriserialize   |


  Scenario Outline: Test the Long URI Deserializer

    Given Test Agent "<uE1>" begins "<Serializer>" test
      And sets "uuri.entity.name" to "body.access"
      And sets "uuri.resource.name" to "door"
      And sets "uuri.resource.instance" to "front_left"
      And sets "uuri.resource.message" to "Door"
    
    When Test Agent "<uE1>" executes "<Deserializer>" on "/body.access//door.front_left#Door"
    # Then Test Agent "<uE1>" receives given protobuf
  
    Examples:

      |    uE1    |     Deserializer          |
      |   python  |     longurideserialize    |
      # |   python  |     microurideserialize    |



  # Scenario Outline: Test cyclic serializer: UUri -> primitive_type -> UUri (original)
  #   Given "<uE1>" creates data for "<Serializer>"
  #     And sets "uri.entity.name" to "body.access"
  #     And sets "uri.resource.name" to "door"
  #     And sets "uri.resource.instance" to "front_left"
  #     And sets "uri.resource.message" to "Door"
  #     And sends "<Serializer>" request
  #     And "<uE1>" receives serialized data

  #   When "<uE2>" sends request to "<Deserializer>" using the serialized data
  #   Then deserialized data from "<uE2>" is equal to data created by "<uE1>"

  #   Examples:

  #   |    uE1    |     Serializer          |    Deserializer     | uE2     |
  #   |   Python  |     longuriserialize    | longurideserialize  | Python  |
  #   #|   Python  |     longuriserialize    | longurideserialize  | Java    |
  #   #|   Java    |     longuriserialize    | longurideserialize  | Python  |
  #   #|   Java    |     longuriserialize    | longurideserialize  | Java  |

  # Scenario Outline: To test the Micro URI Serializers and send apis

  #   Given "<uE1>" creates data for "<Serializer>"
  #     And sets "uri.entity.id" to "1"
  #     And sets "uri.resource.id" to "2"
  #     And sets "uri.authority.id" to "id"
  #     And sends "<Serializer>" request
  #     And "<uE1>" receives serialized data

  #   When "<uE2>" sends request to "<Deserializer>" using the serialized data

  #   Then deserialized data from "<uE2>" is equal to data created by "<uE1>"

  #   Examples:

  #   | uE1       |     Serializer          |     Deserializer     | uE2     |
  #   |   Python  |     microuriserialize   | microurideserialize  | Python  |
  #   #|   Java    |     microuriserialize   | microurideserialize  | Java    |
  #   #|   Python  |     microuriserialize   | microurideserialize  | Java    |
  #   #|   Java    |     microuriserialize   | microurideserialize  | Python  |