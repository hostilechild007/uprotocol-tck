package org.tck.serializer;

import com.google.protobuf.InvalidProtocolBufferException;
import org.json.JSONObject;

import java.util.Map;

public abstract class JsonMessageSerializer {

    public abstract JSONObject execute(JSONObject requestJsonMessage) throws InvalidProtocolBufferException;
}
