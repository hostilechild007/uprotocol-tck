from uprotocol.proto.uri_pb2 import UResource  

class UResourceBuilder:
    def __init__(self) -> None:
        self.name: str = None
        self.instance: str = None
        self.message: str = None
        self.id: int = None
    
    def add_name(self, name: str):
        
        self.name = name
        return self 
    
    def add_instance(self, instance: str):
        
        self.instance = instance
        return self
    
    def add_message(self, message: str):
        
        self.message = message
        return self
    
    def add_id(self, id: int):
        if id < 0:
            raise ValueError("input >= 0")
        
        self.id = id
        return self
    
    def build(self) -> UResource:
        proto = UResource()
            
        if self.name is not None:
            proto.name = self.name
        if self.id is not None:
            proto.id = self.id
        if self.instance is not None:
            proto.instance = self.instance
        if self.message is not None:
            proto.message = self.message
        return proto
    
b = UResourceBuilder().add_name("name").add_message("message").build()
print(b)