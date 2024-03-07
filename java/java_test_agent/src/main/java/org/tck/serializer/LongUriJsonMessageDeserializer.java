/*
 * Copyright (c) 2024 General Motors GTO LLC
 *
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 * SPDX-FileType: SOURCE
 * SPDX-FileCopyrightText: 2024 General Motors GTO LLC
 * SPDX-License-Identifier: Apache-2.0
 */

package org.tck.serializer;

import org.eclipse.uprotocol.cloudevent.serialize.Base64ProtobufSerializer;
import org.eclipse.uprotocol.uri.serializer.LongUriSerializer;
import org.eclipse.uprotocol.v1.UUri;
import org.json.JSONObject;
import org.tck.utils.Constants;

public class LongUriJsonMessageDeserializer extends JsonMessageSerializer {
    @Override
    public JSONObject execute(JSONObject requestJsonMessage) {
        System.out.println("is_serialized_string");
        String uuriSerialized = requestJsonMessage.getString("message");
        UUri uuri = LongUriSerializer.instance().deserialize(uuriSerialized);
        JSONObject responseJson = new JSONObject();
        responseJson.put(Constants.LONG_URI_DESERIALIZE_RESPONSE, Base64ProtobufSerializer.deserialize(uuri.toByteArray()));
        return responseJson;
    }
}
