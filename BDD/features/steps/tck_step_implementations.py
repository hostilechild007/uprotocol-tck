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
from test_manager.testmanager import SocketTestManager

from protobuf_builders.builder import Builder
from protobuf_builders.uentitybuilder import UEntityBuilder
from protobuf_builders.uresourcebuilder import UResourceBuilder
from protobuf_builders.uuribuilder import UUriBuilder
from protobuf_builders.umessagebuilder import UMessageBuilder
from protobuf_builders.upayloadbuilder import UPayloadBuilder
from uprotocol.transport.builder.uattributesbuilder import UAttributesBuilder

from up_client_socket_python.utils.constants import SEND_COMMAND, REGISTER_LISTENER_COMMAND, UNREGISTER_LISTENER_COMMAND, INVOKE_METHOD_COMMAND, LONG_URI_SERIALIZE, LONG_URI_DESERIALIZE, MICRO_URI_SERIALIZE, MICRO_URI_DESERIALIZE

from getters.umessagegetter import UMessageGetter
from getters.upayloadgetter import UPayloadGetter

@given(u'“{sdk_name}” creates data for "{command}"')
@when(u'“{sdk_name}” creates data for "{command}"')
def step_impl(context, sdk_name: str, command: str):
    context.logger.info("Inside create register listener data")
    context.json_array = {}

    while not context.tm.has_sdk_connection(sdk_name):
        continue

    context.ue = sdk_name
    context.json_array['ue'] = [sdk_name]
    context.json_array['action'] = [command]


@given(u'sets "{key}" to "{value}"')
@when(u'sets "{key}" to "{value}"')
def step_impl(context: Context, key: str, value: str):
    '''
    # NOTE: can set like ...
    # And sets "uri.resource.message" to "Door"
    change to 
    And sets "resource.message" to primitive "Door"  -> sets "resource".message = Door
    And sets "uri.resource" to protobuf "resource"  -> uri.resource = resource
    
    Can i prep data w/ data type already when putting value in dict?
    
    '''
    context.logger.info("Json data: Key is " + str(key) + " value is " + str(value))
    if key not in context.json_array:
        context.json_array[key] = [value]


@given(u'sends "{command}" request')
@when(u'sends "{command}" request')
def step_impl(context, command: str):
    context.logger.info(f"Json request for {command} -> {str(context.json_array)}")
    context.status = context.tm.json_action_request(context.json_array)
    context.logger.info(f"Status Received: {context.status}")


@step(u'the status for "{command}" request is "{status}"')
def step_impl(context, command, status):
    context.logger.info(f"Status for {command} is {context.status}")
    assert_that(context.status.message, equal_to(status))


@then(u'"{sdk_name}" receives "{key}" as "{value}"')
def step_impl(context, sdk_name, key, value):
    try:
        if context.tm.received_umessage not in ['', None]:
            received_payload: UPayload = context.tm.received_umessage.payload
            context.logger.info(f"Payload data for {sdk_name} is {received_payload}")
            assert_that(received_payload.value.decode('utf-8'), equal_to(value))
        else:
            raise ValueError(f"Received empty payload for {sdk_name}")

    except AssertionError as ae:
        raise AssertionError(f"Assertion error. Expected is {value} but "
                             f"received {received_payload.value.decode('utf-8')}",
                             exc_info=ae)
        
@given('"{sdk_name}" is connected to the Test Manager')
def tm_connects_to_ta_socket(context, sdk_name: str):
    test_manager: SocketTestManager = context.tm
    
    start_time: float = time.time()
    end_time: float = start_time
    wait_sec: float = 7.0
    
    while not test_manager.has_sdk_connection(sdk_name):
        time.sleep(1)
        end_time = time.time()
    if not test_manager.has_sdk_connection(sdk_name):
        context.logger.error(sdk_name + " Test Agent didn't connect in time")
        raise Exception(sdk_name + " Test Agent didn't connect in time")
    
    context.logger.info(f"{sdk_name} TA connects to TM {test_manager.sdk_to_test_agent_socket.keys()}")


@when('"{sdk_name}" closes its client socket connection')
def tm_closing_ta_socket(context, sdk_name: str):
    test_manager: SocketTestManager = context.tm
    # test_manager.close_ta(sdk_name)
    context.logger.info(f"TM closed TA connection {sdk_name} {test_manager.sdk_to_test_agent_socket.keys()}")
    pass
    
@then('Test Manager closes server socket connection to the "{sdk_name}"')
def step_impl(context, sdk_name: str):
    # context.logger.info("YOOOO SERVER cLOSED")
    pass

@given('protobuf UEntity "{entity}" sets parameter "{param}" equal to string "{value}"')
def initialize_protobuf(context, entity: str, param: str, value: str):    
    if entity not in context.initialized_data:
        context.initialized_data[entity] = UEntityBuilder()
    
    builder: UEntityBuilder = context.initialized_data[entity]
    builder.set(param, value)
        
@given('protobuf UResource "{resrc}" sets parameter "{param}" equal to string "{value}"')
def initialize_protobuf(context, resrc: str, param: str, value: str):
    if resrc not in context.initialized_data:
        context.initialized_data[resrc] = UResourceBuilder()
    
    builder: UResourceBuilder = context.initialized_data[resrc]
    builder.set(param, value)

@given('protobuf UUri "{uuri}" sets parameter "{param}" equal to created protobuf "{value}"')
def initialize_protobuf(context, uuri: str, param: str, value: str):
    if uuri not in context.initialized_data:
        context.initialized_data[uuri] = UUriBuilder()
        
        # can later get filled data directly when send request
        context.initialized_data["uuri_builder"] = context.initialized_data[uuri]
    
    builder: UUriBuilder = context.initialized_data[uuri]
    value_builder: Builder = context.initialized_data[value]
    
    builder.set(param, value_builder.build())
    
@given('protobuf UAttributes "{uattr}" creates publish message with parameter source equal to created protobuf "{value}"')
def initialize_protobuf(context, uattr: str, value: str):
    value_builder: Builder = context.initialized_data[value]
    
    new_builder: UAttributesBuilder = UAttributesBuilder.publish(value_builder.build(), UPriority.UPRIORITY_CS1)
    context.initialized_data[uattr] = new_builder
    context.initialized_data["uattributes_builder"] = new_builder

@given('protobuf UPayload "{payload}" sets parameter "{param}" equal to "{value}"')
def initialize_protobuf(context, payload: str, param: str, value: str):
    if payload not in context.initialized_data:
        context.initialized_data[payload] = UPayloadBuilder()
        
        context.initialized_data["upayload_builder"] = context.initialized_data[payload]
    
    builder: UPayloadBuilder = context.initialized_data[payload]
    builder.set(param, value)

    
@when('Test Manager sends "{command}" request to Test Agent "{sdk_name}"')
def tm_sends_request(context, command: str, sdk_name: str):
    command = command.lower().strip()
    
    if command == REGISTER_LISTENER_COMMAND:
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
    
        
    # wait till TA is connected
    while not context.tm.has_sdk_connection(sdk_name):
        continue
    
    test_manager: SocketTestManager = context.tm
    context.logger.info(f"sdk_name: {sdk_name}; command: {command}")
    context.status = test_manager.request(sdk_name, command, umsg)
    
    context.logger.info("context.status:")
    context.logger.info(context.status)


@when('Test Manager sends "{command}" uri serializer request to Test Agent "{sdk_name}"')
def tm_sends_uri_serializer_request(context, command: str, sdk_name: str):
    command = command.lower().strip()
    
    uuri_builder: UUriBuilder = context.initialized_data["uuri_builder"]
    uuri: UUri = uuri_builder.build()
        
    # wait till TA is connected
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

@then('Test Manager receives an "{status_code}" status for "{command}" request')
def tm_receives_response(context, status_code: str, command: str):
    response_status: UStatus = context.status
    if response_status is None:
        raise ValueError(f"{command} request did not receive a response UStatus")

    status_code = status_code.lower().strip()
    if status_code == "ok":
        assert_that(context.status.code, equal_to(UCode.OK))
        # assert_that(context.status.code, equal_to(UCode.INTERNAL))
    
    # reset status var
    context.status =  None

@then('Test Manager receives OnReceive UMessage from "{sdk_name}" Test Agent with parameter UPayload "{param}" with parameter "{inner_param}" as "{expected}"')
def tm_receives_onreceive(context, sdk_name: str, param: str, inner_param: str, expected: str):
    test_manager: SocketTestManager = context.tm
    
    umsg: UMessage = test_manager.get_onreceive(sdk_name)
    
    umsg_param_getter = UMessageGetter(umsg)
    upay: UPayload = umsg_param_getter.get(param)
    
    actual = UPayloadGetter(upay).get(inner_param)
        
    assert_that(actual.decode('utf-8'), equal_to(expected))
    
@then('Test Manager receives a string "{expected_translation}"')
def tm_receives_serializer_translation(context, expected_translation: str):
    
    if context.translation is None:
        raise ValueError(f"Test Manager did not receive any serializer translation")
    elif not isinstance(context.translation, str):
        raise ValueError(f"Test Manager did not receive string translation")

    actual_translation: str = context.translation 
    context.translation = None
    
    context.logger.info(f"actual_translation: {actual_translation}")
    assert_that(actual_translation, equal_to(expected_translation))