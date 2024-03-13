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
import time
from behave import when, then, given, step
from behave.runner import Context
from hamcrest import assert_that, equal_to

from uprotocol.proto.upayload_pb2 import UPayload
from uprotocol.proto.uri_pb2 import UResource  
from uprotocol.proto.ustatus_pb2 import UStatus
from uprotocol.proto.ustatus_pb2 import UCode
from uprotocol.proto.uri_pb2 import UUri
from uprotocol.proto.uattributes_pb2 import UAttributes, UPriority, UMessageType
from uprotocol.proto.umessage_pb2 import UMessage
from uprotocol.uri.serializer.longuriserializer import LongUriSerializer
from uprotocol.uri.serializer.microuriserializer import MicroUriSerializer
from uprotocol.transport.builder.uattributesbuilder import UAttributesBuilder

import sys
import git
repo = git.Repo('.', search_parent_directories=True)
sys.path.append(repo.working_tree_dir)

from python.protobuf_builders.builder import Builder
from python.protobuf_builders.uentitybuilder import UEntityBuilder
from python.protobuf_builders.uresourcebuilder import UResourceBuilder
from python.protobuf_builders.uuribuilder import UUriBuilder
from python.protobuf_builders.umessagebuilder import UMessageBuilder
from python.protobuf_builders.upayloadbuilder import UPayloadBuilder

from python.utils.constants import SEND_COMMAND, REGISTER_LISTENER_COMMAND, UNREGISTER_LISTENER_COMMAND, INVOKE_METHOD_COMMAND, LONG_URI_SERIALIZE, LONG_URI_DESERIALIZE, MICRO_URI_SERIALIZE, MICRO_URI_DESERIALIZE
from python.test_manager.testmanager import SocketTestManager
from python.getters.umessagegetter import UMessageGetter
from python.getters.upayloadgetter import UPayloadGetter

@given('Test Agent sets UEntity "{entity}" field "{param}" equal to string "{value}"')
def initialize_protobuf(context, entity: str, param: str, value: str):    
    if entity not in context.initialized_data:
        context.initialized_data[entity] = UEntityBuilder()  # cant do THIS
    
    builder: UEntityBuilder = context.initialized_data[entity]
    builder.set(param, value)
        
@given('Test Agent sets UResource "{resrc}" field "{param}" equal to string "{value}"')
def initialize_protobuf(context, resrc: str, param: str, value: str):
    if resrc not in context.initialized_data:
        context.initialized_data[resrc] = UResourceBuilder()
    
    builder: UResourceBuilder = context.initialized_data[resrc]
    builder.set(param, value)

@given('Test Agent sets UUri "{uuri}" field "{param}" equal to created protobuf "{value}"')
def initialize_protobuf(context, uuri: str, param: str, value: str):
    if uuri not in context.initialized_data:
        context.initialized_data[uuri] = UUriBuilder()
        
        context.initialized_data["uuri_builder"] = context.initialized_data[uuri]
    
    builder: UUriBuilder = context.initialized_data[uuri]
    value_builder: Builder = context.initialized_data[value]
    
    builder.set(param, value_builder.build())
    
@given('Test Agent sets UAttributes "{uattr}" creates publish message with parameter source equal to created protobuf "{value}"')
def initialize_protobuf(context, uattr: str, value: str):
    value_builder: Builder = context.initialized_data[value]
    
    new_builder: UAttributesBuilder = UAttributesBuilder.publish(value_builder.build(), UPriority.UPRIORITY_CS1)
    context.initialized_data[uattr] = new_builder
    context.initialized_data["uattributes_builder"] = new_builder

@given('Test Agent sets UPayload "{payload}" field "{param}" equal to "{value}"')
def initialize_protobuf(context, payload: str, param: str, value: str):
    if payload not in context.initialized_data:
        context.initialized_data[payload] = UPayloadBuilder()
        
        context.initialized_data["upayload_builder"] = context.initialized_data[payload]
    
    builder: UPayloadBuilder = context.initialized_data[payload]
    builder.set(param, value)


@when('Test Agent "{sdk_name}" executes "{command}" on given UUri')
def tm_sends_request(context, command: str, sdk_name: str):
    command = command.lower().strip()
    
    if command in [REGISTER_LISTENER_COMMAND, UNREGISTER_LISTENER_COMMAND]:
        uuri_builder: UUriBuilder = context.initialized_data["uuri_builder"]
        uuri: UUri = uuri_builder.build()
        
        umsg: UMessage =  UMessageBuilder().set_uuri(uuri).build()
        
    elif command in [SEND_COMMAND, INVOKE_METHOD_COMMAND]:       
        uuri_builder: UUriBuilder = context.initialized_data["uuri_builder"]
        uuri: UUri = uuri_builder.build()
        
        uattr_builder: UAttributesBuilder = context.initialized_data["uattributes_builder"]
        uattr: UAttributes = uattr_builder.build()
        
        upay_builder: UPayloadBuilder = context.initialized_data["upayload_builder"]
        upayload: UPayload = upay_builder.build()
        
        umsg: UMessage =  UMessageBuilder().set_uuri(uuri).set_payload(upayload).set_attributes(uattr).build()
    
        
    # Wait until TA is connected
    while not context.tm.has_sdk_connection(sdk_name):
        continue
    
    test_manager: SocketTestManager = context.tm
    context.logger.info(f"sdk_name: {sdk_name}; command: {command}")
    
    status: UStatus = test_manager.request(sdk_name, command, umsg)
    context.sdk_to_status[sdk_name] = status
    
    context.logger.info("context.sdk_to_status:")
    context.logger.info(context.sdk_to_status[sdk_name])


@when('Test Manager sends "{command}" uri serializer request to Test Agent "{sdk_name}"')
def tm_sends_uri_serializer_request(context, command: str, sdk_name: str):
    command = command.lower().strip()
    
    uuri_builder: UUriBuilder = context.initialized_data["uuri_builder"]
    uuri: UUri = uuri_builder.build()
        
    # Wait until TA is connected
    while not context.tm.has_sdk_connection(sdk_name):
        continue
    
    test_manager: SocketTestManager = context.tm
    
    if command == LONG_URI_SERIALIZE:
        translation: str = test_manager.uriserializer_request(sdk_name, command, uuri)
    
    elif command == LONG_URI_DESERIALIZE:
        # Input String and TA should respond with UUri proto
        
        topic_str: str = LongUriSerializer().deserialize(uuri)
        translation: UUri = test_manager.uriserializer_request(sdk_name, command, topic_str)
        
    context.translation = translation

@then('Test Agent "{sdk_name}" receives an "{status_code}" status for latest execute')
def tm_receives_response(context, status_code: str, sdk_name: str):
    response_status: UStatus = context.sdk_to_status[sdk_name]
    if response_status is None:
        raise ValueError(f"Request did not receive a response UStatus")

    status_code = status_code.lower().strip()
    if status_code == "ok":
        assert_that(response_status.code, equal_to(UCode.OK))
    
    # Reset status variable
    context.sdk_to_status[sdk_name] =  None

@then('Test Agent "{sdk_name}" builds OnReceive UMessage with parameter UPayload "{param}" with parameter "{inner_param}" as "{expected}"')
def tm_receives_onreceive(context, sdk_name: str, param: str, inner_param: str, expected: str):
    test_manager: SocketTestManager = context.tm
    
    umsg: UMessage = test_manager.get_onreceive(sdk_name)
    
    umsg_param_getter = UMessageGetter(umsg)
    upay: UPayload = umsg_param_getter.get(param)
    
    actual = UPayloadGetter(upay).get(inner_param)
        
    assert_that(actual.decode('utf-8'), equal_to(expected))
    