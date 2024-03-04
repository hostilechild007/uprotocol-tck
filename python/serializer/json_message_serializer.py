from abc import ABC, abstractclassmethod
from typing import Dict

class JsonMessageSerializer(ABC):
    @abstractclassmethod
    def execute(self, request_json_message: Dict[str, str]) -> Dict[str, str]:
        """executes the serializer/deserializer (ex: uri long and micro serializer)

        Args:
            request_json_message (Dict[str, str]): incoming json message with "message" data variable that needs to be serialized/deserialized

        Returns:
            Dict[str, str]: the serialized/deserialized response json message
        """
        pass