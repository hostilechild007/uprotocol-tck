from uprotocol.proto.upayload_pb2 import UPayload, UPayloadFormat


class UPayloadBuilder:
    def __init__(self) -> None:
        self.reference: int = None
        self.value: bytes  = None
        self.length: int = None
        self.format: UPayloadFormat = None

        
    def add_reference(self, reference: int):
        
        self.reference = reference
        self.value = None

        return self
    
    def add_value(self, value: bytes):
        self.reference = None
        self.value = value

        return self
    
    def add_length(self, length: int):
        self.length = length
        return self
    
    def add_format(self, format: UPayloadFormat):
        self.format = format
        return self
    
    def build(self) -> UPayload:
        proto = UPayload()
            
        if self.reference is not None:
            proto.reference = self.reference
        if self.value is not None:
            proto.value = self.value
        if self.length is not None:
            proto.length = self.length
        if self.format is not None:
            proto.format = self.format
        return proto
    
pay = UPayloadBuilder().add_reference(1).add_length(2).add_format(UPayloadFormat.UPAYLOAD_FORMAT_PROTOBUF).build()
print(pay)
