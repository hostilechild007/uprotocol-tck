from typing import Any, Deque, Dict, Union
from collections import deque
from uprotocol.proto.upayload_pb2 import UPayloadFormat
from uprotocol.proto.uattributes_pb2 import UPriority, UMessageType

_upayload_formats = set(UPayloadFormat.keys())
_upriorities = set(UPriority.keys())
_umessage_types = set(UMessageType.keys())


def format_value(value: Union[int, float, str, bytes]):
    if isinstance(value, int) or isinstance(value, float) or isinstance(value, bytes):
        return value
    elif isinstance(value, str):
        if value in _upayload_formats:
            return UPayloadFormat.Value(value)
        elif value in _upriorities:
            return UPriority.Value(value)
        elif value in _umessage_types:
            return UMessageType.Value(value)
        return value
    else:
        raise ValueError(f"JSON Message creation does not handle type {type(value)}")
    
    

def set_json_key(ordered_recursive_fields: Deque[str], value: Any, json: Dict[str, Any]):
    if len(ordered_recursive_fields) == 0:
        return
    
    elif len(ordered_recursive_fields) == 1:
        field = ordered_recursive_fields.popleft()
        json[field] = format_value(value)
        return
    
    else:
        field = ordered_recursive_fields.popleft()
        if field not in json:
            json[field] = {}
            
        json = json[field]

        set_json_key(ordered_recursive_fields, value, json)
        
    
def set_inner_protobuf_fields_in_json(inner_protobuf_fields: str, value, json: Dict[str, Any]):
    
    # get protobuf's recursive fields that need to be set
    ordered_recursive_fields = deque(inner_protobuf_fields.split("."))
    
    # add fields into json 
    set_json_key(ordered_recursive_fields, value, json)
    

# global_json = {}
# set_inner_protobuf_fields_in_json("uri.entity.name", "body.access", global_json)
# set_inner_protobuf_fields_in_json("uri.resource.name", "UPRIORITY_CS2", global_json)
# set_inner_protobuf_fields_in_json("uri.resource.instance", "UMESSAGE_TYPE_PUBLISH", global_json)
# set_inner_protobuf_fields_in_json("uri.resource.message", "UPAYLOAD_FORMAT_TEXT", global_json)
# # set_inner_protobuf_fields_in_json("uri.resource.num", 1, global_json)
# # set_inner_protobuf_fields_in_json("uri.resource.num2", 2.0, global_json)
# # set_inner_protobuf_fields_in_json("uri.resource.bool", True, global_json)
# # set_inner_protobuf_fields_in_json("uri.b.bytes", "basd1", global_json)

# # # Convert dict to string
# # data = json.dumps(global_json)
# # print(data)
# print(global_json)
# print([n for n in UPayloadFormat.keys() ])

# print(format_value("UPAYLOAD_FORMAT_PROTOBUF"))
