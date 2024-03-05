from uprotocol.proto.uri_pb2 import UUri
from uprotocol.uri.serializer.microuriserializer import MicroUriSerializer
from uprotocol.uri.serializer.longuriserializer import LongUriSerializer
from uprotocol.transport.builder.uattributesbuilder import UAttributesBuilder
from protobuf_builders.uauthoritybuilder import UAuthorityBuilder
from protobuf_builders.umessagebuilder import UMessageBuilder

from uprotocol.proto.uattributes_pb2 import UPriority
from uprotocol.proto.ustatus_pb2 import UCode
from uprotocol.proto.ustatus_pb2 import UStatus


uri: str = "/body.access//door.front_left#Door"
topic: UUri = LongUriSerializer().deserialize(uri)

umsg = UMessageBuilder().set_uuri(topic).build()
print(umsg)

def build_uattributes(uuri: UUri):
    
    builder = UAttributesBuilder.publish(uuri, UPriority.UPRIORITY_CS4)
    print(builder.source)
    print("-pp-------")
    return UAttributesBuilder.publish(uuri, UPriority.UPRIORITY_CS4).build()

# build_uattributes(topic)

# s = UStatus(code=UCode.OK, message="OK") 
# print(type(s.code))

# a = UAuthorityBuilder()
# b = a

# a.set_id(b"bytes")
# print(b.id)