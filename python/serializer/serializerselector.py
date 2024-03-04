from typing import Dict
from up_client_socket_python.utils.constants import LONG_URI_SERIALIZE, LONG_URI_DESERIALIZE, MICRO_URI_SERIALIZE, MICRO_URI_DESERIALIZE, LONG_URI_SERIALIZE_RESPONSE, LONG_URI_DESERIALIZE_RESPONSE, MICRO_URI_SERIALIZE_RESPONSE, MICRO_URI_DESERIALIZE_RESPONSE
from serializer.json_message_serializer import JsonMessageSerializer
from serializer.long_uri_json_msg_deserializer import LongUriJsonMessageDeserializer
from serializer.long_uri_json_msg_serializer import LongUriJsonMessageSerializer
from serializer.micro_uri_json_msg_deserializer import MicroUriJsonMessageDeserializer
from serializer.micro_uri_json_msg_serializer import MicroUriJsonMessageSerializer

class JsonMessageSerializerSelector:
    
    def __init__(self) -> None:
        self.name_to_serializer: Dict[str, JsonMessageSerializer] = {
            LONG_URI_SERIALIZE : LongUriJsonMessageSerializer(),
            LONG_URI_DESERIALIZE : LongUriJsonMessageDeserializer(),
            MICRO_URI_SERIALIZE : MicroUriJsonMessageSerializer(),
            MICRO_URI_DESERIALIZE: MicroUriJsonMessageDeserializer()
        }
    
    def select(self, action: str) -> JsonMessageSerializer:
        return self.name_to_serializer[action]