package org.tck.serializer;

import com.google.protobuf.InvalidProtocolBufferException;
import org.eclipse.uprotocol.cloudevent.serialize.Base64ProtobufSerializer;
import org.eclipse.uprotocol.uri.serializer.MicroUriSerializer;
import org.eclipse.uprotocol.v1.UUri;
import org.json.JSONObject;
import org.tck.utils.Constants;

public class MicroUriJsonMessageDeserializer extends JsonMessageSerializer {
    @Override
    public JSONObject execute(JSONObject requestJsonMessage) throws InvalidProtocolBufferException {
        System.out.println("is micro _serialized_ bytes");
        String uuriSerialized = requestJsonMessage.getString("message");
        byte[] uuriSerializedBytes = uuriSerialized.getBytes();
        UUri uuri = MicroUriSerializer.instance().deserialize(uuriSerializedBytes);
        JSONObject responseJson = new JSONObject();
        responseJson.put(Constants.MICRO_URI_DESERIALIZE_RESPONSE, Base64ProtobufSerializer.deserialize(uuri.toByteArray()));
        return responseJson;
    }
}
