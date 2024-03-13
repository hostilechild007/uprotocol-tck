package org.eclipse.uprotocol.tck.testagent;

import java.io.IOException;
import java.net.Socket;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.CompletionStage;
import java.util.concurrent.ExecutionException;

import org.eclipse.uprotocol.rpc.CallOptions;
import org.eclipse.uprotocol.tck.up_client_socket_java.SocketUListener;
import org.eclipse.uprotocol.transport.UListener;
import org.eclipse.uprotocol.transport.builder.UAttributesBuilder;
import org.eclipse.uprotocol.uri.factory.UResourceBuilder;
import org.eclipse.uprotocol.v1.UAttributes;
import org.eclipse.uprotocol.v1.UEntity;
import org.eclipse.uprotocol.v1.UMessage;
import org.eclipse.uprotocol.v1.UPriority;
import org.eclipse.uprotocol.v1.UResource;
import org.eclipse.uprotocol.v1.UStatus;
import org.eclipse.uprotocol.v1.UUri;

public class Test {
    
    public static void main(String[] args) throws IOException, InterruptedException {

        Socket clientSocket = new Socket("127.0.0.5", 12345);
        UListener listener =  new SocketUListener(clientSocket);
        
    	UEntity entity = UEntity.newBuilder().setName("nameJava").setVersionMajor(1).build();
        UResource resrc = UResourceBuilder.forRpcResponse();
        UUri source = UUri.newBuilder().setEntity(entity).setResource(resrc).build();
        UAttributes attributes = UAttributesBuilder.request(source, source, UPriority.UPRIORITY_CS4, 0).build();
    	UMessage umsg = UMessage.newBuilder().setAttributes(attributes).build();
    	


//        UStatus status = TransportLayer.getInstance().unregisterListener(source, listener);
//        System.out.println("Test: unregisterListener");
//        System.out.println(status);
//
        TransportLayer.getInstance().registerListener(source, listener);
        
//      TransportLayer.getInstance().send(umsg);

        CompletionStage<UMessage> response = TransportLayer.getInstance().invokeMethod(umsg.getAttributes().getSource(), umsg.getPayload(), CallOptions.newBuilder().withTimeout(0).build());
        
        CompletableFuture<UMessage> future = response.toCompletableFuture();
        
        
        while (!future.isDone()) {
        	
        }
        
        System.out.println(future.isDone());
        try {
			System.out.println(future.get());
		} catch (InterruptedException | ExecutionException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    }
}
