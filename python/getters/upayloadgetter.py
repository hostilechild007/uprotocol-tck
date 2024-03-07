from uprotocol.proto.upayload_pb2 import UPayload, UPayloadFormat
from up_proto_params_constant.upayload_param_names import REFERENCE_VAR, VALUE_VAR, LENGTH_VAR, FORMAT_VAR


class UPayloadGetter:
    def __init__(self, upayload: UPayload) -> None:
        self.upayload = upayload
    
    def get_reference(self) -> int:
        return self.upayload.reference 
    
    def get_value(self) -> bytes:
        return self.upayload.value
    
    def get_length(self) -> int:
        return self.upayload.length
    
    def get_format(self) -> UPayloadFormat:
        return self.upayload.format 
    
    def get(self, param_name: str):
        
        if param_name == REFERENCE_VAR:
            return self.get_reference()
        elif param_name == VALUE_VAR:
            return self.get_value()
        elif param_name == LENGTH_VAR:
            return self.get_length()
        elif param_name == FORMAT_VAR:
            return self.get_format()
        else:
            raise ValueError(f"{self.__class__.__name__} doesn't handle attribute name {param_name}")