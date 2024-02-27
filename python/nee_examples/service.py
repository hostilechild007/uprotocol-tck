from google.protobuf import any_pb2, empty_pb2
from uprotocol.transport.builder.uattributesbuilder import  UAttributesBuilder
from uprotocol.transport.ulistener import UListener
from uprotocol.proto.uattributes_pb2 import *
from uprotocol.proto.upayload_pb2 import UPayload
from uprotocol.proto.ustatus_pb2 import UStatus
from uprotocol.proto.uattributes_pb2 import UAttributes, UMessageType
from uprotocol.proto.uri_pb2 import UUri
from uprotocol.uri.builder.uresource_builder import UResourceBuilder
from uprotocol.uri.serializer.longuriserializer import LongUriSerializer
# from org_eclipse_uprotocol_zenoh.zenoh_utransport import Zenoh
from up_client_socket_python.transport_layer import TransportLayer

from uprotocol.proto.upayload_pb2 import UPayloadFormat
from google.protobuf.wrappers_pb2 import Int32Value

# from protobuf_builders.uentitybuilder import UEntityBuilder

# from protobuf_builders.uauthoritybuilder import UAuthorityBuilder

# from protobuf_builders.uuribuilder import UUriBuilder


# authority = UAuthorityBuilder().add_id(b"1234").add_ip(b"4321").add_name("name").build()
# entity = UEntityBuilder().add_name("name").add_id(0).add_version_major(1).add_version_minor(2).build()
# resrc = UResourceBuilder().add_name("name").add_message("message").build()

# uuri = UUriBuilder().add_authority(authority).add_entity(entity).add_resource(resrc).build()

class RPCRequestListener(UListener):
    def __init__(self) -> None:
        self.count = 0

    def on_receive(self, topic: UUri, payload: UPayload, attributes: UAttributes) -> UStatus:
        print('on rpc request received')
        # generate any object response
        any_obj = any_pb2.Any()

        any_obj.Pack(Int32Value(value=8))
        payload_data = any_obj.SerializeToString()
        payload = UPayload(value=payload_data,format=payload.format)
        transport = TransportLayer()
        transport.set_socket_config("127.0.0.1", 44444)
        
        attributes = UAttributesBuilder(attributes.id, UMessageType.UMESSAGE_TYPE_RESPONSE, attributes.priority).withReqId(attributes.id).build()
        transport.send(topic, payload, attributes)
        # transport.send(UUri(), payload, attributes)



if __name__ == '__main__':
    # Example payload and attributes
    from uprotocol.proto.uri_pb2 import UUri
    from uprotocol.proto.uri_pb2 import UAuthority
    from uprotocol.proto.uri_pb2 import UEntity
    from uprotocol.proto.uri_pb2 import UResource

    hint = UPayloadFormat.UPAYLOAD_FORMAT_PROTOBUF
    any_obj = any_pb2.Any()
    any_obj.Pack(empty_pb2.Empty())
    payload_data = any_obj.SerializeToString()
    payload = UPayload(value=payload_data, format= hint)
    u_entity = UEntity(name="body.access")
    u_resource = UResourceBuilder.for_rpc_request("ExecuteDoorCommand")
    uri = UUri(entity=u_entity, resource=u_resource)
    transport = TransportLayer()
    transport.set_socket_config("127.0.0.1", 44444)
    transport.register_listener(uri, RPCRequestListener())
    
