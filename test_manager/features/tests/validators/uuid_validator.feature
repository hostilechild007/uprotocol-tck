# -------------------------------------------------------------------------
#
# SPDX-FileCopyrightText: Copyright (c) 2024 Contributors to 
# the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http: *www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# SPDX-FileType: SOURCE
# SPDX-License-Identifier: Apache-2.0
#
# -------------------------------------------------------------------------

Feature: UUID Validation

  Scenario Outline: Given UUIDv8 uProtocol ID, check validation types 1
    # WORKING: uE1 (python) uuid_deserialize then uE2 (python or java) uuid_validate 
    # Problem: uE1 (java) uuid_deserialize DOES NOT WORK b/c java treats longs as SIGNED instead of UNsigned
    Given "uE1" creates data for "uuid_deserialize"

    When sends a "uuid_deserialize" request with serialized input "018f731c-5dc7-8000-8432-4662d3e28404"

    Then receives json with following set fields:
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | msb                  | 112435081377185792            | int                 |
      | lsb                  | 9525753552117597188           | int                 |

    When "uE2" creates data for "uuid_validate"
    And sets "validation_type" to "<validation_type>"
    And sets "uuid" to previous response data
    And sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result             |
      | get_validator   | True        | OK                         |
      | uprotocol       | True        | OK                         |
      | uuidv6          | False       | Not a UUIDv6 Version       |
      | is_uuidv6       | False       |                            |

  Scenario Outline: Given UUIDv8 uProtocol ID, check validation types directly 1
    Given "uE2" creates data for "uuid_validate":
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | uuid.msb             | 112435081377185792            | int                 |
      | uuid.lsb             | 9525753552117597188           | int                 |
    And sets "validation_type" to "<validation_type>"

    When sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result             |
      | get_validator   | True        | OK                         |
      | uprotocol       | True        | OK                         |
      | uuidv6          | False       | Not a UUIDv6 Version       |
      | is_uuidv6       | False       |                            |

  Scenario Outline: Given UUIDv8 uProtocol ID, check validation types 2
    Given "uE1" creates data for "uuid_deserialize"

    When sends a "uuid_deserialize" request with serialized input "018f731c-9a33-8000-b377-b346116e27f8"

    Then receives json with following set fields:
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | msb                  | 112435082390896640            | int                 |
      | lsb                  | 12932001968539183096          | int                 |

    When "uE2" creates data for "uuid_validate"
    And sets "validation_type" to "<validation_type>"
    And sets "uuid" to previous response data
    And sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result             |
      | get_validator   | True        | OK                         |
      | uprotocol       | True        | OK                         |
      | uuidv6          | False       | Not a UUIDv6 Version       |
      | is_uuidv6       | False       |                            |

  Scenario Outline: Given UUIDv8 uProtocol ID, check validation types directly 2
    Given "uE2" creates data for "uuid_validate":
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | uuid.msb             | 112435082390896640            | int                 |
      | uuid.lsb             | 12932001968539183096          | int                 |
    And sets "validation_type" to "<validation_type>"

    When sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result             |
      | get_validator   | True        | OK                         |
      | uprotocol       | True        | OK                         |
      | uuidv6          | False       | Not a UUIDv6 Version       |
      | is_uuidv6       | False       |                            |

  Scenario Outline: Given UUIDv8 uProtocol ID, check validation types 3
    Given "uE1" creates data for "uuid_deserialize"

    When sends a "uuid_deserialize" request with serialized input "018f731d-6375-8000-baca-67403cc85e2b"

    Then receives json with following set fields:
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | msb                  | 112435085767442432            | int                 |
      | lsb                  | 13459683961945480747          | int                 |

    When "uE2" creates data for "uuid_validate"
    And sets "validation_type" to "<validation_type>"
    And sets "uuid" to previous response data
    And sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result             |
      | get_validator   | True        | OK                         |
      | uprotocol       | True        | OK                         |
      | uuidv6          | False       | Not a UUIDv6 Version       |
      | is_uuidv6       | False       |                            |

  Scenario Outline: Given UUIDv8 uProtocol ID, check validation types directly 3
    Given "uE2" creates data for "uuid_validate":
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | uuid.msb             | 112435085767442432            | int                 |
      | uuid.lsb             | 13459683961945480747          | int                 |
    And sets "validation_type" to "<validation_type>"

    When sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result             |
      | get_validator   | True        | OK                         |
      | uprotocol       | True        | OK                         |
      | uuidv6          | False       | Not a UUIDv6 Version       |
      | is_uuidv6       | False       |                            |

  Scenario Outline: Given invalid uProtocol ID UUID(msb=0, lsb=0), check validation types
    Given "uE1" creates data for "uuid_deserialize"

    When sends a "uuid_deserialize" request with serialized input "00000000-0000-0000-0000-000000000000"

    Then receives json with following set fields:
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | msb                  | 0                             | int                 |
      | lsb                  | 0                             | int                 |

    When "uE2" creates data for "uuid_validate"
    And sets "validation_type" to "<validation_type>"
    And sets "uuid" to previous response data
    And sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result                                               |
      | get_validator   | False       | Invalid UUID Version,Invalid UUID Variant,Invalid UUID Time  |
      | uprotocol       | False       | Invalid UUIDv8 Version,Invalid UUID Time                     |
      | uuidv6          | False       | Not a UUIDv6 Version,Invalid UUIDv6 variant,Invalid UUID Time|
      | is_uuidv6       | False       |                                                              |

  Scenario Outline: Given invalid uProtocol ID UUID(msb=0, lsb=0), directly check validation types
    Given "uE2" creates data for "uuid_validate":
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | uuid.msb             | 0                             | int                 |
      | uuid.lsb             | 0                             | int                 |
    And sets "validation_type" to "<validation_type>"

    When sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result                                               |
      | get_validator   | False       | Invalid UUID Version,Invalid UUID Variant,Invalid UUID Time  |
      | uprotocol       | False       | Invalid UUIDv8 Version,Invalid UUID Time                     |
      | uuidv6          | False       | Not a UUIDv6 Version,Invalid UUIDv6 variant,Invalid UUID Time|
      | is_uuidv6       | False       |                                                              |

  Scenario Outline: Given valid time UUIDv8 uProtocol ID, check validation types 1
    Given "uE1" creates data for "uuid_deserialize"

    When sends a "uuid_deserialize" request with serialized input "018f7744-85a5-8000-8e60-93e2a8a4e9da"

    Then receives json with following set fields:
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | msb                  | 112439651891249152            | int                 |
      | lsb                  | 10259362552851261914          | int                 |

    When "uE2" creates data for "uuid_validate"
    And sets "validation_type" to "<validation_type>"
    And sets "uuid" to previous response data
    And sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result       |
      | get_validator   | True        | OK                   |
      | uprotocol       | True        | OK                   |
      | uuidv6          | False       | Not a UUIDv6 Version |
      | is_uuidv6       | False       |                      |

  Scenario Outline: Given valid time UUIDv8 uProtocol ID, directly check validation types 1
    Given "uE2" creates data for "uuid_deserialize":
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | uuid.msb             | 112439651891249152            | int                 |
      | uuid.lsb             | 10259362552851261914          | int                 |
    And sets "validation_type" to "<validation_type>"

    When sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result       |
      | get_validator   | True        | OK                   |
      | uprotocol       | True        | OK                   |
      | uuidv6          | False       | Not a UUIDv6 Version |
      | is_uuidv6       | False       |                      |

  Scenario Outline: Given valid time UUIDv8 uProtocol ID, check validation types 2
    Given "uE1" creates data for "uuid_deserialize"

    When sends a "uuid_deserialize" request with serialized input "000004e3-3880-8000-8895-b64c80d87c13"

    Then receives json with following set fields:
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | msb                  | 5373952032768                 | int                 |
      | lsb                  | 9841973000383527955           | int                 |

    When "uE2" creates data for "uuid_validate"
    And sets "validation_type" to "<validation_type>"
    And sets "uuid" to previous response data
    And sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result       |
      | get_validator   | True        | OK                   |
      | uprotocol       | True        | OK                   |
      | uuidv6          | False       | Not a UUIDv6 Version |
      | is_uuidv6       | False       |                      |


  Scenario Outline: Given valid time UUIDv8 uProtocol ID, directly check validation types 2
    Given "uE2" creates data for "uuid_deserialize":
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | uuid.msb             | 5373952032768                 | int                 |
      | uuid.lsb             | 9841973000383527955           | int                 |
    And sets "validation_type" to "<validation_type>"

    When sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result       |
      | get_validator   | True        | OK                   |
      | uprotocol       | True        | OK                   |
      | uuidv6          | False       | Not a UUIDv6 Version |
      | is_uuidv6       | False       |                      |

  Scenario Outline: Given invalid time UUIDv8 uProtocol ID, check validation types 3
    Given "uE1" creates data for "uuid_deserialize"

    When sends a "uuid_deserialize" request with serialized input "00000000-0000-8000-ae60-e898b2ada5e2"

    Then receives json with following set fields:
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | msb                  | 32768                         | int                 |
      | lsb                  | 12565298702894081506          | int                 |

    When "uE2" creates data for "uuid_validate"
    And sets "validation_type" to "<validation_type>"
    And sets "uuid" to previous response data
    And sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result       |
      | get_validator   | False       | Invalid UUID Time    |
      | uprotocol       | False       | Invalid UUID Time    |
      | uuidv6          | False       | Not a UUIDv6 Version,Invalid UUID Time |
      | is_uuidv6       | False       |                      |

  Scenario Outline: Given invalid time UUIDv8 uProtocol ID, directly check validation types 3
    Given "uE2" creates data for "uuid_deserialize":
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | uuid.msb             | 32768                         | int                 |
      | uuid.lsb             | 12565298702894081506          | int                 |
    And sets "validation_type" to "<validation_type>"

    When sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result       |
      | get_validator   | False       | Invalid UUID Time    |
      | uprotocol       | False       | Invalid UUID Time    |
      | uuidv6          | False       | Not a UUIDv6 Version,Invalid UUID Time |
      | is_uuidv6       | False       |                      |

  Scenario Outline: Given valid  UUIDv6 uProtocol ID, check validation types 1
    Given "uE1" creates data for "uuid_deserialize"

    When sends a "uuid_deserialize" request with serialized input "1ef1218f-908e-6ae1-9fc5-cc0dc557b1ff"

    Then receives json with following set fields:
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | msb                  | 2229600191014398689           | int                 |
      | lsb                  | 11512832381960040959          | int                 |

    When "uE2" creates data for "uuid_validate"
    And sets "validation_type" to "<validation_type>"
    And sets "uuid" to previous response data
    And sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result        |
      | get_validator   | True        | OK                    |
      | uprotocol       | False       | Invalid UUIDv8 Version|
      | uuidv6          | True        | OK                    |
      | is_uuidv6       | True        |                       |

  Scenario Outline: Given valid  UUIDv6 uProtocol ID, directly check validation types 1
    Given "uE2" creates data for "uuid_deserialize":
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | uuid.msb             | 2229600191014398689           | int                 |
      | uuid.lsb             | 11512832381960040959          | int                 |
    And sets "validation_type" to "<validation_type>"

    When sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result        |
      | get_validator   | True        | OK                    |
      | uprotocol       | False       | Invalid UUIDv8 Version|
      | uuidv6          | True        | OK                    |
      | is_uuidv6       | True        |                       |

  Scenario Outline: Given valid  UUIDv6 uProtocol ID, check validation types 2
    Given "uE1" creates data for "uuid_deserialize"

    When sends a "uuid_deserialize" request with serialized input "1ef12198-332a-64ad-8f5a-3a56320be567"

    Then receives json with following set fields:
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | msb                  | 2229600228102268077           | int                 |
      | lsb                  | 10329632837208892775          | int                 |

    When "uE2" creates data for "uuid_validate"
    And sets "validation_type" to "<validation_type>"
    And sets "uuid" to previous response data
    And sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result        |
      | get_validator   | True        | OK                    |
      | uprotocol       | False       | Invalid UUIDv8 Version|
      | uuidv6          | True        | OK                    |
      | is_uuidv6       | True        |                       |

  Scenario Outline: Given valid  UUIDv6 uProtocol ID, directly check validation types 2
    Given "uE2" creates data for "uuid_deserialize":
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | uuid.msb             | 2229600228102268077           | int                 |
      | uuid.lsb             | 10329632837208892775          | int                 |
    And sets "validation_type" to "<validation_type>"

    When sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result        |
      | get_validator   | True        | OK                    |
      | uprotocol       | False       | Invalid UUIDv8 Version|
      | uuidv6          | True        | OK                    |
      | is_uuidv6       | True        |                       |

  Scenario Outline: Given valid  UUIDv6 uProtocol ID, check validation types 3
    Given "uE1" creates data for "uuid_deserialize"

    When sends a "uuid_deserialize" request with serialized input "1ef1219f-e1d0-61f4-b5ed-2dd36670ae65"

    Then receives json with following set fields:
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | msb                  | 2229600261097153012           | int                 |
      | lsb                  | 13109184476325391973          | int                 |

    When "uE2" creates data for "uuid_validate"
    And sets "validation_type" to "<validation_type>"
    And sets "uuid" to previous response data
    And sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result        |
      | get_validator   | True        | OK                    |
      | uprotocol       | False       | Invalid UUIDv8 Version|
      | uuidv6          | True        | OK                    |
      | is_uuidv6       | True        |                       |
  
  Scenario Outline: Given valid  UUIDv6 uProtocol ID, directly check validation types 3
    Given "uE2" creates data for "uuid_deserialize":
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | uuid.msb             | 2229600261097153012           | int                 |
      | uuid.lsb             | 13109184476325391973          | int                 |
    And sets "validation_type" to "<validation_type>"

    When sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result        |
      | get_validator   | True        | OK                    |
      | uprotocol       | False       | Invalid UUIDv8 Version|
      | uuidv6          | True        | OK                    |
      | is_uuidv6       | True        |                       |

  Scenario Outline: Given valid time UUIDv6 uProtocol ID, check validation types 4
    Given "uE1" creates data for "uuid_deserialize"

    When sends a "uuid_deserialize" request with serialized input "1ef121b3-828a-6203-b213-976dbd2b73b3"

    Then receives json with following set fields:
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | msb                  | 2229600345398075907           | int                 |
      | lsb                  | 12831766260889646003          | int                 |

    When "uE2" creates data for "uuid_validate"
    And sets "validation_type" to "<validation_type>"
    And sets "uuid" to previous response data
    And sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result        |
      | get_validator   | True        | OK                    |
      | uprotocol       | False       | Invalid UUIDv8 Version|
      | uuidv6          | True        | OK                    |
      | is_uuidv6       | True        |                       |

  Scenario Outline: Given valid  UUIDv6 uProtocol ID, directly check validation types 4
    Given "uE2" creates data for "uuid_deserialize":
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | uuid.msb             | 2229600345398075907           | int                 |
      | uuid.lsb             | 12831766260889646003          | int                 |
    And sets "validation_type" to "<validation_type>"

    When sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result        |
      | get_validator   | True        | OK                    |
      | uprotocol       | False       | Invalid UUIDv8 Version|
      | uuidv6          | True        | OK                    |
      | is_uuidv6       | True        |                       |

  Scenario Outline: Given UUIDv4 uProtocol ID, check validation types 
    Given "uE1" creates data for "uuid_deserialize"

    When sends a "uuid_deserialize" request with serialized input "195f9bd1-526d-4c28-91b1-ff34c8e3632d"

    Then receives json with following set fields:
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | msb                  | 1828351297069075496           | int                 |
      | lsb                  | 10498452808551064365          | int                 |

    When "uE2" creates data for "uuid_validate"
    And sets "validation_type" to "<validation_type>"
    And sets "uuid" to previous response data
    And sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result                                             |
      | get_validator   | False       | Invalid UUID Version,Invalid UUID Variant,Invalid UUID Time |
      | uprotocol       | False       | Invalid UUIDv8 Version,Invalid UUID Time                   |
      | uuidv6          | False       | Not a UUIDv6 Version,Invalid UUID Time                     |
      | is_uuidv6       | False       |                                                            |

  Scenario Outline: Given valid  UUIDv6 uProtocol ID, directly check validation types 4
    Given "uE2" creates data for "uuid_deserialize":
      | protobuf_field_names | protobuf_field_values         | protobuf_field_type |
      | uuid.msb             | 1828351297069075496           | int                 |
      | uuid.lsb             | 10498452808551064365          | int                 |
    And sets "validation_type" to "<validation_type>"

    When sends "uuid_validate" request

    Then receives validation result as "<bool_result>"
    And  receives validation message as "<message_result>"

    Examples:
      | validation_type | bool_result | message_result                                             |
      | get_validator   | False       | Invalid UUID Version,Invalid UUID Variant,Invalid UUID Time |
      | uprotocol       | False       | Invalid UUIDv8 Version,Invalid UUID Time                   |
      | uuidv6          | False       | Not a UUIDv6 Version,Invalid UUID Time                     |
      | is_uuidv6       | False       |                                                            |