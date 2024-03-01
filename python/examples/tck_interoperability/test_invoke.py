from up_client_socket_python.socket_utransport import SocketUTransport
from multimethod import multimethod
import time
from threading import Thread
from typing import Dict, List
from google.protobuf.any_pb2 import Any
from concurrent.futures import Future, ThreadPoolExecutor

from uprotocol.proto.uattributes_pb2 import UAttributes
from uprotocol.proto.uri_pb2 import UUri
from uprotocol.proto.ustatus_pb2 import UStatus
from uprotocol.proto.ustatus_pb2 import UStatus, UCode
from uprotocol.transport.ulistener import UListener
from uprotocol.proto.umessage_pb2 import UMessage

from uprotocol.proto.cloudevents_pb2 import CloudEvent
from uprotocol.proto.upayload_pb2 import UPayload, UPayloadFormat
from uprotocol.proto.uattributes_pb2 import UPriority
from uprotocol.transport.builder.uattributesbuilder import UAttributesBuilder
from uprotocol.uri.serializer.longuriserializer import LongUriSerializer
from up_client_socket_python.transport_layer import TransportLayer
from test_manager.testmanager import SocketTestManager

uri: str = "/body.access//door.front_left#Door"


def build_cloud_event(source: str, id: str = "fake id"):
    return CloudEvent(spec_version="1.0", source=source, id="I am " + id)


@multimethod
def build_upayload(source: str, id: str, ):
    any_obj = Any()
    any_obj.Pack(build_cloud_event(source, id))
    return UPayload(format=UPayloadFormat.UPAYLOAD_FORMAT_PROTOBUF, value=any_obj.SerializeToString())


@multimethod
def build_upayload(cloud_event: CloudEvent):
    any_obj = Any()
    any_obj.Pack(cloud_event)
    return UPayload(format=UPayloadFormat.UPAYLOAD_FORMAT_PROTOBUF, value=any_obj.SerializeToString())


@multimethod
def build_upayload(sdk: str):
    any_obj = Any()
    any_obj.Pack(build_cloud_event(sdk))
    return UPayload(format=UPayloadFormat.UPAYLOAD_FORMAT_PROTOBUF, value=any_obj.SerializeToString())


def build_uattributes():
    return UAttributesBuilder.publish(UPriority.UPRIORITY_CS4).build()


PORT = 44444
IP = "127.0.0.1"
socketTrans = SocketUTransport(IP, PORT)
topic = LongUriSerializer().deserialize(uri)
payload: UPayload = build_upayload("python")
attributes: UAttributes = build_uattributes()

response: Future = socketTrans.invoke_method(topic, payload, attributes)
print(response)
while not response.done():
    pass

print(response.result(), response.done())
