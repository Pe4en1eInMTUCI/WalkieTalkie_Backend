package me.Pe4en1e;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.eclipse.jetty.websocket.api.RemoteEndpoint;
import org.eclipse.jetty.websocket.api.Session;
import org.eclipse.jetty.websocket.api.annotations.OnWebSocketClose;
import org.eclipse.jetty.websocket.api.annotations.OnWebSocketConnect;
import org.eclipse.jetty.websocket.api.annotations.OnWebSocketMessage;
import org.eclipse.jetty.websocket.api.annotations.WebSocket;

import javax.xml.crypto.Data;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

@WebSocket
public class WebSocketEndpoint {

    private final List<Session> active = new ArrayList<>();

    @OnWebSocketConnect
    public void clientConnect(Session session) throws InterruptedException, IOException {
        System.out.println("New connection: " + session.getRemoteAddress().toString());

    }

    @OnWebSocketClose
    public void clientDisconnect(Session session) {
        System.out.println("Client disconnect: " + session.getRemoteAddress().toString());


    }

    @OnWebSocketMessage
    public void clientMessage(Session session, String message) throws IOException {


        ObjectMapper mapper = new ObjectMapper();

        JsonNode node = mapper.readTree(message);

        System.out.println("from: " + node.get("from").asText());
        System.out.println("to: " + node.get("to").asText());
        System.out.println("content: " + node.get("content").asText());
        System.out.println("chat_id: " + node.get("chat_id").asText());



    }

}
