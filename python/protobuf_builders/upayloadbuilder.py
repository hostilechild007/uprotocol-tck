from uprotocol.proto.upayload_pb2 import UPayload, UPayloadFormat
from protobuf_builders.builder import Builder

from up_client_socket_python.utils.grammar_parsing_utils import get_umessage_type


REFERENCE_VAR: str = "reference"
VALUE_VAR: str = "value"
LENGTH_VAR: str = "length"
FORMAT_VAR: str = "format"

class UPayloadBuilder(Builder):
    def __init__(self) -> None:
        self.reference: int = None
        self.value: bytes  = None
        self.length: int = None
        self.format: UPayloadFormat = None

    def set_reference(self, reference: int):
        
        self.reference = reference
        self.value = None

        return self
    
    def set_value(self, value: bytes):
        self.reference = None
        self.value = value

        return self
    
    def set_length(self, length: int):
        self.length = length
        return self
    
    def set_format(self, format: UPayloadFormat):
        self.format = format
        return self

    def set(self, attribute_name: str, attribute_value: str):
        attribute_name = attribute_name.lower().strip()
        
        if attribute_name == REFERENCE_VAR:
            return self.set_reference(int(attribute_value))
        elif attribute_name == VALUE_VAR:
            return self.set_value(attribute_value.encode())
        elif attribute_name == LENGTH_VAR:
            return self.set_length(int(attribute_value))
        elif attribute_name == FORMAT_VAR:
            return self.set_format(get_umessage_type(attribute_value))
        else:
            raise ValueError(f"{self.__class__.__name__} doesn't handle attribute name {attribute_name}")
    
    def build(self) -> UPayload:
        proto = UPayload()
            
        if self.reference is not None:
            proto.reference = self.reference
        if self.value is not None:
            proto.value = self.value
        if self.length is not None:
            proto.length = self.length
        if self.format is not None:
            print("here")
            proto.format = self.format
        return proto

# print( UPayloadBuilder().set_reference(1).set_value(b"value").set_length(0).set_format(get_umessage_type("UMESSAGE_TYPE_UNSPECIFIED")).build() )
# print( UPayloadBuilder().set("reference", "1").set("value", "value").set("length", "0").set("format", "UMESSAGE_TYPE_UNSPECIFIED").build() )