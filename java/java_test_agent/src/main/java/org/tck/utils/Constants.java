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

package org.tck.utils;

import java.util.HashSet;
import java.util.Set;

public class Constants {
    public static final String SEND_COMMAND = "send";
    public static final String REGISTER_LISTENER_COMMAND = "registerlistener";
    public static final String UNREGISTER_LISTENER_COMMAND = "unregisterlistener";
    public static final String INVOKE_METHOD_COMMAND = "invokemethod";
    public static Set<String> COMMANDS = new HashSet<>();

    static {
        COMMANDS.add(SEND_COMMAND);
        COMMANDS.add(REGISTER_LISTENER_COMMAND);
        COMMANDS.add(UNREGISTER_LISTENER_COMMAND);
        COMMANDS.add(INVOKE_METHOD_COMMAND);
    }

    public static final String LONG_URI_SERIALIZE = "longuriserialize";
    public static final String LONG_URI_DESERIALIZE = "longurideserialize";
    public static final String MICRO_URI_SERIALIZE = "microuriserialize";
    public static final String MICRO_URI_DESERIALIZE = "microurideserialize";
    public static Set<String> SERIALIZERS = new HashSet<>();

    static {
        SERIALIZERS.add(LONG_URI_SERIALIZE);
        SERIALIZERS.add(LONG_URI_DESERIALIZE);
        SERIALIZERS.add(MICRO_URI_SERIALIZE);
        SERIALIZERS.add(MICRO_URI_DESERIALIZE);
    }

    public static final String LONG_URI_SERIALIZE_RESPONSE = "longuriserialize_response";
    public static final String LONG_URI_DESERIALIZE_RESPONSE = "longurideserialize_response";
    public static final String MICRO_URI_SERIALIZE_RESPONSE = "microuriserialize_response";
    public static final String MICRO_URI_DESERIALIZE_RESPONSE = "microurideserialize_response";

}
