package org.tck.serializer;

import org.tck.utils.Constants;

import java.util.HashMap;
import java.util.Map;

public class JsonMessageSerializerSelector {
    private Map<String, JsonMessageSerializer> nameToSerializer;

    public JsonMessageSerializerSelector() {
        nameToSerializer = new HashMap<>();
        nameToSerializer.put(Constants.LONG_URI_SERIALIZE, new LongUriJsonMessageSerializer());
        nameToSerializer.put(Constants.LONG_URI_DESERIALIZE, new LongUriJsonMessageDeserializer());
        nameToSerializer.put(Constants.MICRO_URI_SERIALIZE, new MicroUriJsonMessageSerializer());
        nameToSerializer.put(Constants.MICRO_URI_DESERIALIZE, new MicroUriJsonMessageDeserializer());
    }

    public JsonMessageSerializer select(String action) {
        return nameToSerializer.get(action);
    }
}
