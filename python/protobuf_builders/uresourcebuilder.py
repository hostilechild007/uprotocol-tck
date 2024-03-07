from uprotocol.proto.uri_pb2 import UResource  
from protobuf_builders.builder import Builder

NAME_VAR: str = "name"
ID_VAR: str = "id"
MESSAGE_VAR: str = "message"
INSTANCE_VAR: str = "instance"

class UResourceBuilder(Builder):
    def __init__(self) -> None:
        self.name: str = None
        self.instance: str = None
        self.message: str = None
        self.id: int = None
    
    def set_name(self, name: str):
        
        self.name = name
        return self 
    
    def set_instance(self, instance: str):
        
        self.instance = instance
        return self
    
    def set_message(self, message: str):
        
        self.message = message
        return self
    
    def set_id(self, id: int):
        
        self.id = id
        return self
    
    def set(self, attribute_name: str, attribute_value: str):
        attribute_name = attribute_name.lower().strip()
        
        if attribute_name == NAME_VAR:
            return self.set_name(attribute_value)
        elif attribute_name == ID_VAR:
            return self.set_id(int(attribute_value))
        elif attribute_name == INSTANCE_VAR:
            return self.set_instance(attribute_value)
        elif attribute_name == MESSAGE_VAR:
            return self.set_message(attribute_value)
        else:
            raise ValueError(f"{self.__class__.__name__} doesn't handle attribute name {attribute_name}")
    
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
    

# print( UResourceBuilder().set("name", "name").set("id", "1").set("instance", "instance").set("message", "message").build() )