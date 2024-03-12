package org.eclipse.uprotocol.tck.testagent;

import java.io.IOException;
import java.net.Socket;

import org.eclipse.uprotocol.rpc.CallOptions;
import org.eclipse.uprotocol.tck.up_client_socket_java.SocketUListener;
import org.eclipse.uprotocol.transport.UListener;
import org.eclipse.uprotocol.v1.UMessage;
import org.eclipse.uprotocol.v1.UUri;

public class Test {
    
    public static void main(String[] args) throws IOException {
        TransportLayer.getInstance().send(UMessage.getDefaultInstance());
        System.out.println("Test: Sent");

        Socket clientSocket = new Socket("127.0.0.5", 12345);
        System.out.println("Connected to TM");
        UListener listener =  new SocketUListener(clientSocket);

        TransportLayer.getInstance().registerListener(UUri.getDefaultInstance(), listener);
        System.out.println("Test: RegisterListener");

        TransportLayer.getInstance().unregisterListener(UUri.getDefaultInstance(), listener);
        System.out.println("Test: unregisterListener");

        TransportLayer.getInstance().registerListener(UUri.getDefaultInstance(), listener);
        System.out.println("Test: RegisterListener");

        TransportLayer.getInstance().invokeMethod(UMessage.getDefaultInstance().getAttributes().getSource(), UMessage.getDefaultInstance().getPayload(), CallOptions.newBuilder().withTimeout(0).build());
    }
}
