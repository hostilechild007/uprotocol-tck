
from typing import Dict

from uprotocol.proto.uri_pb2 import UUri
from uprotocol.uri.serializer.longuriserializer import LongUriSerializer

from serializer.json_message_serializer import JsonMessageSerializer
from up_client_socket_python.utils.socket_message_processing_utils import protobuf_to_base64, create_json_message
from up_client_socket_python.utils.constants import LONG_URI_DESERIALIZE_RESPONSE


class LongUriJsonMessageDeserializer(JsonMessageSerializer):
    def execute(self, request_json_message: Dict[str, str]) -> Dict[str, str]:
        print("is_serialized_string")
        uuri_serialized: str = request_json_message["message"]

        uuri: UUri = LongUriSerializer().deserialize(uuri_serialized)

        # response_json: Dict[str, str] = {
        #     "action": LONG_URI_DESERIALIZE_RESPONSE,
        #     "message": protobuf_to_base64(uuri)
        # }
        return create_json_message(LONG_URI_DESERIALIZE_RESPONSE, protobuf_to_base64(uuri))