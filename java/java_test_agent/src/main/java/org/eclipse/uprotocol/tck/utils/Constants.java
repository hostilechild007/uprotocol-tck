package org.eclipse.uprotocol.tck.utils;

import java.util.HashSet;
import java.util.Set;

public class Constants {
    public static final String SEND_COMMAND = "send";
    public static final String REGISTER_LISTENER_COMMAND = "registerlistener";
    public static final String UNREGISTER_LISTENER_COMMAND = "unregisterlistener";
    public static final String INVOKE_METHOD_COMMAND = "invokemethod";
    public static Set<String> COMMANDS = new HashSet<>();

    static {
        COMMANDS.add(SEND_COMMAND);
        COMMANDS.add(REGISTER_LISTENER_COMMAND);
        COMMANDS.add(UNREGISTER_LISTENER_COMMAND);
        COMMANDS.add(INVOKE_METHOD_COMMAND);
    }
}
