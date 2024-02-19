package me.Pe4en1e;

import org.eclipse.jetty.websocket.api.Session;
import org.eclipse.jetty.websocket.api.annotations.OnWebSocketClose;
import org.eclipse.jetty.websocket.api.annotations.OnWebSocketConnect;
import org.eclipse.jetty.websocket.api.annotations.OnWebSocketMessage;
import org.eclipse.jetty.websocket.api.annotations.WebSocket;

import java.io.IOException;

@WebSocket
public class WebSocketEndpoint {

    @OnWebSocketConnect
    public void clientConnect(Session session) throws InterruptedException, IOException {
        System.out.println("New connection: " + session.getRemoteAddress().toString());
        DataSender dataSender = new DataSender();
        dataSender.sendData(session);
    }

    @OnWebSocketClose
    public void clientDisconnect(Session session) {
        System.out.println("Client disconnect: " + session.getRemoteAddress().toString());

    }

    @OnWebSocketMessage
    public void clientMessage(Session session, String message) throws IOException {
        System.out.println(session.getRemoteAddress() + ": " + message);
    }

}
