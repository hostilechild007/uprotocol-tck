package org.tck.serializer;

import org.eclipse.uprotocol.cloudevent.serialize.Base64ProtobufSerializer;
import org.eclipse.uprotocol.uri.serializer.LongUriSerializer;
import org.eclipse.uprotocol.v1.UUri;
import org.json.JSONObject;
import org.tck.utils.Constants;

public class LongUriJsonMessageDeserializer extends JsonMessageSerializer {
    @Override
    public JSONObject execute(JSONObject requestJsonMessage) {
        System.out.println("is_serialized_string");
        String uuriSerialized = requestJsonMessage.getString("message");
        UUri uuri = LongUriSerializer.instance().deserialize(uuriSerialized);
        JSONObject responseJson = new JSONObject();
        responseJson.put(Constants.LONG_URI_DESERIALIZE_RESPONSE, Base64ProtobufSerializer.deserialize(uuri.toByteArray()));
        return responseJson;
    }
}
