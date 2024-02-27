from uprotocol.proto.uri_pb2 import UUri, UAuthority, UEntity, UResource
from uprotocol.uri.serializer.longuriserializer import LongUriSerializer
from uprotocol.rpc.rpcmapper import RpcMapper
from google.protobuf.any_pb2 import Any
import socket
from multipledispatch import dispatch
from uprotocol.proto.umessage_pb2 import UMessage
from multimethod import multimethod
from up_client_socket_python.utils.socket_message_processing_utils import convert_json_to_jsonstring
from concurrent.futures import Future, ThreadPoolExecutor
import time
from socket_rpcclient import SocketRPCClient
'''class Class:
    @multimethod
    def _send_to_test_agent(self, test_agent_socket: socket.socket, command: str, umsg: UMessage):
        print("send_to_test_agent")
        

    @multimethod
    def _send_to_test_agent(self, test_agent_socket: socket.socket, protobuf: Any):
        print("hrtr")
        
    def call(self):
        self._send_to_test_agent(socket.socket(socket.AF_INET, socket.SOCK_STREAM), "str", UMessage())
    
Class().call()'''

def method():
    
    response.set_result("meow")

response = Future()
print( response.done())
method()
time.sleep(1)
print("fin")
print(response.result(), response.done())