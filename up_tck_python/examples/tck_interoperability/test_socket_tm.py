import time

from google.protobuf.any_pb2 import Any
from concurrent.futures import ThreadPoolExecutor

from uprotocol.proto.uattributes_pb2 import UAttributes
from uprotocol.proto.uri_pb2 import UUri
from uprotocol.proto.ustatus_pb2 import UStatus
from uprotocol.proto.ustatus_pb2 import UStatus, UCode
from uprotocol.transport.ulistener import UListener

from uprotocol.proto.cloudevents_pb2 import CloudEvent
from uprotocol.proto.upayload_pb2 import UPayload, UPayloadFormat
from uprotocol.proto.uattributes_pb2 import UPriority
from uprotocol.transport.builder.uattributesbuilder import UAttributesBuilder
from uprotocol.uri.serializer.longuriserializer import LongUriSerializer
from up_tck_python.up_client_socket_python.transport_layer import TransportLayer
from up_tck_python.test_manager.testmanager import SocketTestManager

import logging 

logging.basicConfig(format='%(asctime)s %(message)s')
# Create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

transport = TransportLayer()
transport.set_socket_config("127.0.0.1", 44444)
manager = SocketTestManager("127.0.0.5", 12345, transport)


uri: str = "/body.access//door.front_left#Door"

def build_cloud_event(id: str):
    return CloudEvent(spec_version="1.0", source="https://example.com", id="I am " + id)

def build_upayload(id: str):
    any_obj = Any()
    any_obj.Pack(build_cloud_event(id))
    return UPayload(format=UPayloadFormat.UPAYLOAD_FORMAT_PROTOBUF, value=any_obj.SerializeToString())

def build_uattributes():
    return UAttributesBuilder.publish(UPriority.UPRIORITY_CS4).build()

class SocketUListener(UListener):
    def __init__(self) -> None:
        pass

    def on_receive(self, topic: UUri, payload: UPayload, attributes: UAttributes) -> UStatus:
        """
        Method called to handle/process events.<br><br>
        @param topic: Topic the underlying source of the message.
        @param payload: Payload of the message.
        @param attributes: Transportation attributes.
        @return Returns an Ack every time a message is received and processed.
        """
        logger.info("Listener onreceived")
        logger.info("MATTHEW is awesome!!!")

        logger.info(f"{payload}")

        return UStatus(code=UCode.OK, message="all good") 


listener: UListener = SocketUListener()

with ThreadPoolExecutor(max_workers=1) as executor:
    # submit the task
    future = executor.submit(manager.listen_for_client_connections)
    time.sleep(10)

    while True:
        sdk: str = input("Enter SDK Language[java/python]: ")
        sdk = sdk.strip()
        command_name = input("Enter Command Name[send/registerlistener]: ")
        command_name = command_name.strip().lower()

        topic = LongUriSerializer().deserialize(uri)
        payload: UPayload = build_upayload(sdk)
        attributes: UAttributes = build_uattributes()

        if command_name == "send": 
            print("SEND COMMAND")
            status: UStatus = manager.send_command(sdk, command_name, topic, payload, attributes)
        elif command_name == "registerlistener":
            status: UStatus = manager.register_listener_command(sdk, command_name, topic, listener)
        else:
            print("in exception!")
            continue
        print("sdk:", sdk)
        print("status:", status)
        print("---------------")