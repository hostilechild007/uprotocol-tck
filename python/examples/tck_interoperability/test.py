from uprotocol.proto.uri_pb2 import UUri
from uprotocol.uri.serializer.microuriserializer import MicroUriSerializer
from uprotocol.uri.serializer.longuriserializer import LongUriSerializer


uri: str = "/body.access//door.front_left#Door"
topic: UUri = LongUriSerializer().deserialize(uri)
print(topic)
topic_b: bytearray = MicroUriSerializer().serialize(topic)

print(bytes(topic_b))
print(topic_b.decode())