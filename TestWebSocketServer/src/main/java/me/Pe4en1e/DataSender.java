package me.Pe4en1e;

import org.eclipse.jetty.websocket.api.Session;

import java.io.IOException;

public class DataSender {

    public void sendData(Session session) {
        try {
            while (true) {
                session.getRemote().sendString("Some data!");
                Thread.sleep(1000);
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
