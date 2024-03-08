from google.protobuf import any_pb2, empty_pb2
from uprotocol.transport.builder.uattributesbuilder import  UAttributesBuilder
from uprotocol.transport.ulistener import UListener
from uprotocol.proto.uattributes_pb2 import *
from uprotocol.proto.upayload_pb2 import UPayload
from uprotocol.proto.ustatus_pb2 import UStatus
from uprotocol.proto.uattributes_pb2 import UAttributes, UPriority, UMessageType
from uprotocol.proto.uri_pb2 import UUri
from uprotocol.uri.factory.uresource_builder import UResourceBuilder
from uprotocol.uri.serializer.longuriserializer import LongUriSerializer
# from org_eclipse_uprotocol_zenoh.zenoh_utransport import Zenoh
from uprotocol.proto.umessage_pb2 import UMessage

from uprotocol.proto.upayload_pb2 import UPayloadFormat
from google.protobuf.wrappers_pb2 import Int32Value

import git
import sys
sys.path.append("../")

repo = git.Repo('.', search_parent_directories=True)
sys.path.append(repo.working_tree_dir)
from python.test_agent.transport_layer import TransportLayer

class RPCRequestListener(UListener):

    def on_receive(self, umsg: UMessage) -> UStatus:
        
        topic: UUri = umsg.attributes.source 
        payload: UPayload = umsg.payload
        attributes: UAttributes = umsg.attributes
        
        print('on rpc request received')
        # generate any object response
        any_obj = any_pb2.Any()

        any_obj.Pack(Int32Value(value=8))
        payload_data = any_obj.SerializeToString()
        payload = UPayload(value=payload_data,format=payload.format)        
        attributes = UAttributesBuilder(topic, attributes.id, UMessageType.UMESSAGE_TYPE_RESPONSE, attributes.priority).withReqId(attributes.id).build()
        
        transport = TransportLayer()
        msg = UMessage(attributes=attributes, payload=payload)
        transport.send(msg)


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
    transport.register_listener(uri, RPCRequestListener())
