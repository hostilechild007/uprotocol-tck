from uprotocol.uuid.factory.uuidfactory import Factories
from uprotocol.proto.uuid_pb2 import UUID
from datetime import datetime, timezone
from uprotocol.uuid.serializer.longuuidserializer import LongUuidSerializer
from uprotocol.uuid.validate.uuidvalidator import UuidValidator, Validators
from uprotocol.uuid.factory.uuidutils import UUIDUtils

uprotocol = Factories.UPROTOCOL.create()
# print(type(uprotocol))
# print(uprotocol)
print(UUIDUtils.is_uprotocol(uprotocol))

uproto_v8_validator: UuidValidator = UuidValidator.get_validator(uprotocol)
print(uproto_v8_validator.validate(uprotocol))
print(Validators.UPROTOCOL.validator().validate(uprotocol))
print(Validators.UUIDV6.validator().validate(uprotocol))
print(UUIDUtils.is_uuidv6(uprotocol))

give_uuid = UUID(msb=112435085767442432, lsb=13459683961945480747)
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

print("----")
invalid = UUID(msb=0, lsb=0)
print(type(invalid))
print(invalid)
print(UUIDUtils.is_uprotocol(invalid))

print("---")
uprotocol_time = Factories.UPROTOCOL.create(
            datetime.utcfromtimestamp(0).replace(tzinfo=timezone.utc)
        )
print(type(uprotocol_time))
print("time:", uprotocol_time)

print("---")
uuidv6 = Factories.UUIDV6.create()
print(type(uuidv6))
print(uuidv6)
print(UUIDUtils.is_uprotocol(uuidv6))

print("---")
uuidv4 = LongUuidSerializer().deserialize("195f9bd1-526d-4c28-91b1-ff34c8e3632d")
print(type(uuidv4))
print(uuidv4)
print(UUIDUtils.is_uprotocol(uuidv4))
