from protobuf_builders.builder import Builder
from uprotocol.proto.umessage_pb2 import UMessage
from uprotocol.proto.uattributes_pb2 import UAttributes
from uprotocol.proto.uri_pb2 import UUri
from uprotocol.proto.upayload_pb2 import UPayload

class UMessageBuilder(Builder):
    def __init__(self) -> None:
        self.attributes: UAttributes = None
        self.payload: UPayload = None
        self.uuri: UUri = None
        
    def set_attributes(self, attributes: UAttributes):
        self.attributes = attributes
        return self
    
    def set_payload(self, payload: UPayload):
        self.payload = payload
        return self
    
    def set_uuri(self, uuri: UUri):
        self.uuri = uuri
        return self
    
    def build(self) -> UMessage:
        
        proto = UMessage()
        
        if self.attributes is not None:
            proto.attributes.CopyFrom(self.attributes)            
        if self.payload is not None:
            proto.payload.CopyFrom(self.payload)
        if self.uuri is not None:
            if self.attributes is None:
                proto.attributes.CopyFrom(UAttributes())
            proto.attributes.source.CopyFrom(self.uuri)
            
        return proto