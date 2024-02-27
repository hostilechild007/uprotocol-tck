from uprotocol.proto.uri_pb2 import UEntity 

class UEntityBuilder:
    def __init__(self) -> None:
        self.name: str = None
        self.id: int = None
        self.version_major: int = None
        self.version_minor: int = None
    
    def add_name(self, name: str):
        
        self.name = name
        return self
    
    def add_id(self, id : int):
        if id < 0:
            raise ValueError("input >= 0")
        self.id = id

        return self
    
    def add_version_major(self, version_major: int):
        if version_major < 0:
            raise ValueError("input >= 0")

        self.version_major = version_major

        return self
    
    def add_version_minor(self, version_minor : int):
        if version_minor < 0:
            raise ValueError("input >= 0")

        self.version_minor = version_minor 

        return self
    
    def build(self) -> UEntity:
        """

        @return Returns a constructed
        """
        proto = UEntity()
            
        if self.name is not None:
            proto.name = self.name
        if self.id is not None:
            proto.id = self.id
        if self.version_major is not None:
            proto.version_major = self.version_major
        if self.version_minor is not None:
            proto.version_minor = self.version_minor
        return proto
    
u = UEntityBuilder().add_name("name").add_id(0).add_version_major(1).add_version_minor(2).build()
print(u)