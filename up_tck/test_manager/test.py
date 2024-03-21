
from up_tck.python_utils.constants import UTransportRequestCommand


print("send" in UTransportRequestCommand.COMMANDS.value)
print("send" == UTransportRequestCommand.SEND.value)
print("send" == UTransportRequestCommand.REGISTER_LISTENER.value)