# -------------------------------------------------------------------------
#
# Copyright (c) 2023 General Motors GTO LLC
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
# SPDX-FileCopyrightText: 2023 General Motors GTO LLC
# SPDX-License-Identifier: Apache-2.0
#
# -------------------------------------------------------------------------

import uuid


class ReqCodeRPC:
    """
    Class containing command codes related to RPC functionality.
    """
    CMD_RPC = 'CMD_RPC'


class ReqCodePUBSUB:
    """
    Class containing command codes related to PUBSUB functionality.
    """
    CMD_PUB_SUB_MULTIPROCESS = 'CMD_PUB_SUB_MULTIPROCESS'
    CMD_ZENOH_PUB_SUB = 'CMD_ZENOH_PUB_SUB'
    CMD_ZENOH_PUB_SOMEIP_SUB = 'CMD_ZENOH_PUB_SOMEIP_SUB'
    CMD_SOMEIP_PUB_ZENOH_SUB = 'CMD_SOMEIP_PUB_ZENOH_SUB'


class ReqIDUtils:
    """
    Utility class for generating request IDs.
    """

    @staticmethod
    def generate_request_id() -> uuid.UUID:
        """
        Generate a UUIDv4
        Returns:  A UUIDv4 id.
        """
        return uuid.uuid4()
