from uprotocol.proto.uri_pb2 import UUri
from uprotocol.uri.serializer.microuriserializer import MicroUriSerializer
from uprotocol.uri.serializer.longuriserializer import LongUriSerializer
from uprotocol.transport.builder.uattributesbuilder import UAttributesBuilder
from protobuf_builders.uauthoritybuilder import UAuthorityBuilder
from protobuf_builders.umessagebuilder import UMessageBuilder
from protobuf_builders.upayloadbuilder import UPayloadBuilder

from uprotocol.proto.uattributes_pb2 import UPriority
from uprotocol.proto.ustatus_pb2 import UCode
from uprotocol.proto.ustatus_pb2 import UStatus


uri: str = "/body.access//door.front_left#Door"
topic: UUri = LongUriSerializer().deserialize(uri)

def build_uattributes(uuri: UUri):
    
    builder = UAttributesBuilder.publish(uuri, UPriority.UPRIORITY_CS4)

    return UAttributesBuilder.publish(uuri, UPriority.UPRIORITY_CS4).build()

attr = build_uattributes(topic)
pay = UPayloadBuilder().set("reference", "1").set("value", "value").set("length", "0").set("format", "UPAYLOAD_FORMAT_UNSPECIFIED").build()

umsg = UMessageBuilder().set_uuri(topic).set_attributes(attr).set_payload(pay).build()
print(umsg)

# s = UStatus(code=UCode.OK, message="OK") 
# print(type(s.code))

# a = UAuthorityBuilder()
# b = a

# a.set_id(b"bytes")
# print(b.id)