package org.tck.utils;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Constants {
    public static final String SEND_COMMAND = "send";
    public static final String REGISTER_LISTENER_COMMAND = "registerlistener";
    public static final String UNREGISTER_LISTENER_COMMAND = "unregisterlistener";
    public static final String INVOKE_METHOD_COMMAND = "invokemethod";
    public static Set<String> COMMANDS = new HashSet<>();

    static{
        COMMANDS.add(SEND_COMMAND);
        COMMANDS.add(REGISTER_LISTENER_COMMAND);
        COMMANDS.add(UNREGISTER_LISTENER_COMMAND);
        COMMANDS.add(INVOKE_METHOD_COMMAND);
    }

    public static final String LONG_URI_SERIALIZE = "longuriserialize";
    public static final String LONG_URI_DESERIALIZE = "longurideserialize";
    public static final String MICRO_URI_SERIALIZE = "microuriserialize";
    public static final String MICRO_URI_DESERIALIZE = "microurideserialize";
    public static Set<String> SERIALIZERS = new HashSet<>();

    static {
        SERIALIZERS.add(LONG_URI_SERIALIZE);
        SERIALIZERS.add(LONG_URI_DESERIALIZE);
        SERIALIZERS.add(MICRO_URI_SERIALIZE);
        SERIALIZERS.add(MICRO_URI_DESERIALIZE);
    }

    public static final String LONG_URI_SERIALIZE_RESPONSE = "longuriserialize_response";
    public static final String LONG_URI_DESERIALIZE_RESPONSE = "longurideserialize_response";
    public static final String MICRO_URI_SERIALIZE_RESPONSE = "microuriserialize_response";
    public static final String MICRO_URI_DESERIALIZE_RESPONSE = "microurideserialize_response";

}
