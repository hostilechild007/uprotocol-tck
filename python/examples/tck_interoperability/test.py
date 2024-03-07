from uprotocol.proto.uri_pb2 import UUri
from uprotocol.proto.uri_pb2 import UEntity 
from uprotocol.proto.uri_pb2 import UAuthority
from uprotocol.proto.uri_pb2 import UResource  

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


u_entity = UEntity(name="body.access")
u_resource = UResource(name="door", instance="front_left", message="Door")
uri = UUri(entity=u_entity,resource= u_resource)

s = LongUriSerializer().serialize(uri)
print(s)