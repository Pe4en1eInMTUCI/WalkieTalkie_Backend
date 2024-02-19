package me.Pe4en1e;

import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.servlet.ServletContextHandler;
import org.eclipse.jetty.websocket.server.config.JettyWebSocketServletContainerInitializer;

import java.time.Duration;

public class Main {
    public static void main(String[] args) {

        Main main = new Main();
        main.run();
    }


    public void run() {
        Server server = new Server(9043);
        var handler = new ServletContextHandler(server, "/api");
        server.setHandler(handler);


        JettyWebSocketServletContainerInitializer.configure(handler, ((servletContext, container) -> {
            container.setIdleTimeout(Duration.ofMinutes(5));
            container.addMapping("/", WebSocketEndpoint.class);
        }));

        try {
            server.start();
            System.out.println("Server started!");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}