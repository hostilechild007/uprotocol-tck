from uprotocol.proto.uri_pb2 import UUri
from uprotocol.uri.serializer.microuriserializer import MicroUriSerializer
from uprotocol.uri.serializer.longuriserializer import LongUriSerializer
from uprotocol.transport.builder.uattributesbuilder import UAttributesBuilder
from uprotocol.proto.uattributes_pb2 import UPriority


uri: str = "/body.access//door.front_left#Door"
topic: UUri = LongUriSerializer().deserialize(uri)

def build_uattributes(uuri: UUri):
    
    builder = UAttributesBuilder.publish(uuri, UPriority.UPRIORITY_CS4)
    print(builder.source)
    print("-pp-------")
    return UAttributesBuilder.publish(uuri, UPriority.UPRIORITY_CS4).build()

build_uattributes(topic)