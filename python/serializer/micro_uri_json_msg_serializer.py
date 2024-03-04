
from typing import Dict
from google.protobuf.any_pb2 import Any

from uprotocol.proto.uri_pb2 import UUri
from uprotocol.rpc.rpcmapper import RpcMapper
from uprotocol.uri.serializer.microuriserializer import MicroUriSerializer

from serializer.json_message_serializer import JsonMessageSerializer
from up_client_socket_python.utils.socket_message_processing_utils import base64_to_protobuf_bytes, create_json_message
from up_client_socket_python.utils.constants import MICRO_URI_SERIALIZE_RESPONSE

class MicroUriJsonMessageSerializer(JsonMessageSerializer):
    def execute(self, request_json_message: Dict[str, str]) -> Dict[str, str]:
        print("is_ micro serialized_protobuf")
        uuri_base64: str = request_json_message["message"]
        protobuf_serialized_data: bytes = base64_to_protobuf_bytes(uuri_base64)  
    
        uuri: UUri = RpcMapper.unpack_payload(Any(value=protobuf_serialized_data), UUri)
        
        uuri_serialized: bytes = MicroUriSerializer().serialize(uuri)
        
        print("uuri_serialized.decode()", uuri_serialized.decode())
        response_json: Dict[str, str] = create_json_message(MICRO_URI_SERIALIZE_RESPONSE, uuri_serialized.decode())
        return response_json