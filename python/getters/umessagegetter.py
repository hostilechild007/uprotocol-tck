from uprotocol.proto.umessage_pb2 import UMessage
from uprotocol.proto.uri_pb2 import UUri
from uprotocol.proto.upayload_pb2 import UPayload
from uprotocol.proto.uattributes_pb2 import UAttributes


SOURCE_VAR: str = "source"
PAYLOAD_VAR: str = "payload"
ATTRIBUTES_VAR: str = "attribute"

class UMessageGetter:
    def __init__(self, umsg: UMessage) -> None:        
        self.umsg: UMessage = umsg
        
    def get_source(self) -> UUri:
        return self.umsg.attributes.source
    
    def get_payload(self) -> UPayload:
        return self.umsg.payload
    
    def get_attributes(self) -> UAttributes:
        return self.umsg.attributes
    
    def get(self, param_name: str):
        param_name = param_name.lower().strip()
        
        if param_name == SOURCE_VAR:
            return self.get_source()
        elif param_name == PAYLOAD_VAR:
            return self.get_payload()
        elif param_name == ATTRIBUTES_VAR:
            return self.get_attributes()
        else:
            raise ValueError(f"{self.__class__.__name__} doesn't have param {param_name}")