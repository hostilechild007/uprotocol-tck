import time
from uprotocol.uuid.factory.uuidfactory import Factories
from uprotocol.proto.uuid_pb2 import UUID
from datetime import datetime, timezone
from uprotocol.uuid.serializer.longuuidserializer import LongUuidSerializer
from uprotocol.uuid.validate.uuidvalidator import UuidValidator, Validators, UUIDv6Validator, UUIDv8Validator
from uprotocol.uuid.factory.uuidutils import UUIDUtils

def print_validator(uuid: UUID):
    uproto_v8_validator: UuidValidator = UuidValidator.get_validator(uuid)
    print(uproto_v8_validator.validate(uuid))
    print(Validators.UPROTOCOL.validator().validate(uuid))
    print(Validators.UUIDV6.validator().validate(uuid))
    print(UUIDUtils.is_uuidv6(uuid))

uprotocol = Factories.UPROTOCOL.create()
# print(type(uprotocol))
# print(uprotocol)
print(UUIDUtils.is_uprotocol(uprotocol))

print_validator(uprotocol)

give_uuid = UUID(msb=1, lsb=1)
serialized = LongUuidSerializer().serialize(give_uuid)
print(give_uuid, "\n", serialized)


'''
msb: 112435081377185792
lsb: 9525753552117597188

msb: 112435082390896640
lsb: 12932001968539183096

msb: 112435085767442432
lsb: 13459683961945480747
'''

# print("--Invalid--")
# invalid = UUID(msb=0, lsb=0)
# print("serialized invalid:", LongUuidSerializer().serialize(invalid))
# print(type(invalid))
# print(invalid)
# print(UUIDUtils.is_uprotocol(invalid))
# print_validator(invalid)


# print("--Time--")
# print(datetime.fromtimestamp(1545730073).replace(tzinfo=timezone.utc))
# print(datetime.fromtimestamp(100000).replace(tzinfo=timezone.utc))

# uprotocol_time = Factories.UPROTOCOL.create(
#             datetime.fromtimestamp(100000).replace(tzinfo=timezone.utc)
#         )
# print("serialized time:", LongUuidSerializer().serialize(uprotocol_time))

# print(type(uprotocol_time))
# print("time:", uprotocol_time)
# print_validator(uprotocol_time)

# print("---time 2---")
# uprotocol_time = Factories.UPROTOCOL.create(
#             datetime.fromtimestamp(time.time()).replace(tzinfo=timezone.utc)
#         )
# print("uuid:", uprotocol_time)

# print("serialized time:", LongUuidSerializer().serialize(uprotocol_time))
# print(UUIDUtils.get_time(uprotocol_time))
# print_validator(uprotocol_time)

# print("---time 3---")
# uprotocol_time = Factories.UPROTOCOL.create(
#             datetime.utcfromtimestamp(0).replace(tzinfo=timezone.utc)
#         )
# print("uuid:", uprotocol_time)

# print("serialized time:", LongUuidSerializer().serialize(uprotocol_time))
# print(UUIDUtils.get_time(uprotocol_time))
# print_validator(uprotocol_time)

# print("--UUIDV6--")
# uuidv6 = Factories.UUIDV6.create()
# print("serialized uuidv6:", LongUuidSerializer().serialize(uuidv6))
# print(type(uuidv6))
# print(uuidv6)
# print(UUIDUtils.is_uprotocol(uuidv6))
# print_validator(uuidv6)

# print("--UUIDV6 time--")
# uuidv6_time = Factories.UUIDV6.create(datetime.fromtimestamp(time.time()).replace(tzinfo=timezone.utc))
# print("serialized uuidv6:", LongUuidSerializer().serialize(uuidv6_time))
# print(type(uuidv6_time))
# print(uuidv6_time)
# print(UUIDUtils.is_uprotocol(uuidv6_time))
# print_validator(uuidv6_time)

# print("--UUIDV6 bad time--")
# uuidv6_time = Factories.UUIDV6.create(datetime.utcfromtimestamp(0).replace(tzinfo=timezone.utc))
# print("serialized uuidv6:", LongUuidSerializer().serialize(uuidv6_time))
# print(type(uuidv6_time))
# print(uuidv6_time)
# print(UUIDUtils.is_uprotocol(uuidv6_time))
# print_validator(uuidv6_time)

# print("--uuidv4-")
# uuidv4 = LongUuidSerializer().deserialize("195f9bd1-526d-4c28-91b1-ff34c8e3632d")
# print(type(uuidv4))
# print(uuidv4)
# print(UUIDUtils.is_uprotocol(uuidv4))
# print_validator(uuidv4)

# print("////")
# uprotocol_time = Factories.UPROTOCOL.create(
#             datetime.utcfromtimestamp(0).replace(tzinfo=timezone.utc)
#         )
# print(uprotocol_time)
# print(UUIDv8Validator().validate_time(uprotocol_time))
# uprotocol_time = Factories.UUIDV6.create(
#             datetime.utcfromtimestamp(0).replace(tzinfo=timezone.utc)
#         )
# print(uprotocol_time, type(uprotocol_time))
# print(UUIDv6Validator().validate_time(uprotocol_time))