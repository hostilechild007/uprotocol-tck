from abc import ABC, abstractclassmethod

class Builder(ABC):
    
    # @abstractclassmethod
    # def add(self, attribute_name: str, attribute_value: str):
    #     pass
    
    @abstractclassmethod
    def build(self):
        pass