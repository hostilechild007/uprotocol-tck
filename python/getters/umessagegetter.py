from uprotocol.proto.umessage_pb2 import UMessage
from uprotocol.proto.uri_pb2 import UUri
from uprotocol.proto.upayload_pb2 import UPayload
from uprotocol.proto.uattributes_pb2 import UAttributes

class UMessageGetter:
    def __init__(self, umsg: UMessage) -> None:
        self.umsg: UMessage = umsg
        
    def get_uuri(self) -> UUri:
        return self.umsg.attributes.source
    
    def get_upayload(self) -> UPayload:
        return self.umsg.payload
    
    def get_uattribtes(self) -> UAttributes:
        return self.umsg.attributes