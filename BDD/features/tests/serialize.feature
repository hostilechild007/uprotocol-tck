Scenario Outline: To test the Serializers and send apis
    Given manager creates data for "<Serializer>" for “<uE1>”
      And sets "uri.entity.name" to "body.access"
      And sets "uri.resource.name" to "door"
      And sets "uri.resource.instance" to "front_left"
      And sets "uri.resource.message" to "Door"
      And sends "<Serializer>" request to "<uE1>"
      And the status for "<Serializer>" request is "OK"

	Then manager receives serialized data from "<uE1>"

	Given manager creates data for "<Serializer>" for "<uE2>"
		And sets "serializeddata" to "context.serialized_data"
		and sends "serializeddata" request to "<uE2>"
		And the status for "<Serializer>" request is "OK"
	
	Then manager receives deserialized data from "<uE1>" as "deserializeddatafrombefore"
	

1. TM -> *sends uuri -> TA (serializes uuri data into a string) -> *replies w/ new string -> TM -> *sends new string -> TA2 (deserizalize it to UURI) -> *sends uuri -> TM

Examples:

| uE1       |     Serializer-Deserializer     | uE2     |
|   Python  |     MicroUri                    | Python  |
|   Java    |     MicroUri                    | Java    |
|   Python  |     Long Uri                    | Java    |
|   Java    |     Long Uri                    | Python  |