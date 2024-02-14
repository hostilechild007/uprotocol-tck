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

import json
import uuid
from test_request.utils.request_utils import ReqIDUtils, ReqCodePUBSUB


class PUBSUBRequest:
    """
    Class representing a PUBSUB request.

    Attributes:
       id (uuid.UUID): The unique identifier for the request. If not provided, a new UUIDv4 is generated.
       code (str): The code associated with the request.
       ip_address (str): The IP address associated with the request.
       event_instance (int): The event instance associated with the request.
       topics (int): The number of topics associated with the request.
       events (int): The number of events associated with the request.
       interval (int): The interval associated with the request, measured in milliseconds.
       publisher_processes (int): The number of publisher processes associated with the request.
       subscriber_processes (int): The number of subscriber processes associated with the request.
       timeout (int): The timeout associated with the request, measured in milliseconds.
    """

    def __init__(self, code: str = '', ip_address: str = '', event_instance: int = 0,
                 topics: int = 0, events: int = 0, interval: int = 0, publisher_processes: int = 0,
                 subscriber_processes: int = 0, timeout: int = 0, id: uuid.UUID = None):
        """
        Initialize a PUBSUBRequest instance.

        Parameters:
            code (str): The code associated with the request.
            ip_address (str): The IP address associated with the request.
            event_instance (int): The event instance associated with the request.
            topics (int): The number of topics associated with the request.
            events (int): The number of events associated with the request.
            interval (int): The interval associated with the request, measured in milliseconds.
            publisher_processes (int): The number of publisher processes associated with the request.
            subscriber_processes (int): The number of subscriber processes associated with the request.
            timeout (int): The timeout associated with the request, measured in milliseconds.
            id (uuid.UUID): The unique identifier for the request. If not provided, a new UUIDv4 is generated.
        """
        self.id = id or ReqIDUtils.generate_request_id()
        self.code = code
        self.ip_address = ip_address
        self.event_instance = event_instance
        self.topics = topics
        self.events = events
        self.interval = interval
        self.publisher_processes = publisher_processes
        self.subscriber_processes = subscriber_processes
        self.timeout = timeout

    def to_json_string(self) -> str:
        """
        Convert the PUBSUBRequest instance to a JSON-formatted string.
        Returns: str: JSON-formatted string representing the PUBSUBRequest.
        """
        json_dict = self.__dict__.copy()
        json_dict['ip-address'] = json_dict.pop('ip_address')
        json_dict['event-instance'] = json_dict.pop('event_instance')
        json_dict['publisher-processes'] = json_dict.pop('publisher_processes')
        json_dict['subscriber-processes'] = json_dict.pop('subscriber_processes')
        if 'id' in json_dict:
            json_dict['id'] = str(json_dict['id'])
        return json.dumps(json_dict)


if __name__ == "__main__":
    # Example usage:
    pub_sub_request_json_string = PUBSUBRequest(code=ReqCodePUBSUB.CMD_PUB_SUB_MULTIPROCESS, ip_address='127.0.0.1',
                                                event_instance=1, interval=5,
                                                publisher_processes=3, subscriber_processes=2,
                                                timeout=10).to_json_string()
    print(pub_sub_request_json_string)
