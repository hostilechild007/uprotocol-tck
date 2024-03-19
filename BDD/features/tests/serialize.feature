Feature: Serializer and Deserializer Testing
Scenario Outline: To test the Long URI Serializers and send apis
    Given "<uE1>" creates data for "<Serializer>"
      And sets "uri.entity.name" to "body.access"
      And sets "uri.resource.name" to "door"
      And sets "uri.resource.instance" to "front_left"
      And sets "uri.resource.message" to "Door"
      And sends "<Serializer>" request
      And "<uE1>" receives serialized data

	When "<uE2>" sends request to "<Deserializer>" using the serialized data
	Then deserialized data from "<uE2>" is equal to data created by "<uE1>"

Examples:

|    uE1    |     Serializer          |    Deserializer     | uE2     |
|   Python  |     longuriserialize    | longurideserialize  | Python  |
#|   Python  |     longuriserialize    | longurideserialize  | Java    |
#|   Java    |     longuriserialize    | longurideserialize  | Python  |
#|   Java    |     longuriserialize    | longurideserialize  | Java  |

Scenario Outline: To test the Micro URI Serializers and send apis

    Given "<uE1>" creates data for "<Serializer>"
      And sets "uri.entity.id" to "1"
      And sets "uri.resource.id" to "2"
      And sets "uri.authority.id" to "id"
      And sends "<Serializer>" request
     And "<uE1>" receives serialized data

    When "<uE2>" sends request to "<Deserializer>" using the serialized data

	Then deserialized data from "<uE2>" is equal to data created by "<uE1>"

Examples:

| uE1       |     Serializer          |     Deserializer     | uE2     |
|   Python  |     microuriserialize   | microurideserialize  | Python  |
#|   Java    |     microuriserialize   | microurideserialize  | Java    |
#|   Python  |     microuriserialize   | microurideserialize  | Java    |
#|   Java    |     microuriserialize   | microurideserialize  | Python  |