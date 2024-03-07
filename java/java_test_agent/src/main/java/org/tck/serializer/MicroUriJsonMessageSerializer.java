package org.tck.serializer;

import com.google.protobuf.InvalidProtocolBufferException;
import org.eclipse.uprotocol.cloudevent.serialize.Base64ProtobufSerializer;
import org.eclipse.uprotocol.uri.serializer.MicroUriSerializer;
import org.eclipse.uprotocol.v1.UUri;
import org.json.JSONObject;
import org.tck.utils.Constants;

public class MicroUriJsonMessageSerializer extends JsonMessageSerializer {


    @Override
    public JSONObject execute(JSONObject requestJsonMessage) throws InvalidProtocolBufferException {
        System.out.println("is_ micro serialized_protobuf");
        String uuriBase64 = requestJsonMessage.getString("message");
        byte[] protobuf_serialized_data = Base64ProtobufSerializer.serialize(uuriBase64);
        UUri uuri = UUri.parseFrom(protobuf_serialized_data);
        byte[] uuriSerialized = MicroUriSerializer.instance().serialize(uuri);
        System.out.println("uuri_serialized.decode() " + uuriSerialized);
        JSONObject responseJson = new JSONObject();
        responseJson.put(Constants.MICRO_URI_SERIALIZE_RESPONSE, uuriSerialized);
        return responseJson;
    }
}
