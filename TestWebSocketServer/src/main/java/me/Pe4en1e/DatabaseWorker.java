package me.Pe4en1e;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class DatabaseWorker {

    static final String DB_URL = "jdbc:mysql://147.45.138.238/default_db";
    static final String USER = "gen_user";
    static final String PASS = "Ib&c5<ysBY}l71";

    public boolean addMessage(int chat_id, String from, String to, String content) {

        try {

            Connection connection = DriverManager.getConnection(DB_URL, USER, PASS);

            PreparedStatement preparedStatement = connection.prepareStatement("INSERT INTO messages VALUES (?, ?, ?, ?)");

            preparedStatement.setInt(1, chat_id);
            preparedStatement.setString(2, from);
            preparedStatement.setString(3, to);
            preparedStatement.setString(4, content);

            preparedStatement.executeUpdate();

            connection.close();

            return true;

        } catch (Exception e) {
            System.out.println(e.getMessage());
            return false;
        }
    }

    public void setUserOnline(String userID) {

        try {
            Connection connection = DriverManager.getConnection(DB_URL, USER, PASS);

            PreparedStatement preparedStatement = connection.prepareStatement("UPDATE users SET isOnline = 1 WHERE userID = ?");

            preparedStatement.setString(1, userID);

            preparedStatement.executeUpdate();

            connection.close();

            return;
        } catch (Exception e) {
            System.out.println(e.getMessage());
            return;
        }

    }

    public  void setUserOffline(String userID) {
        try {
            Connection connection = DriverManager.getConnection(DB_URL, USER, PASS);

            PreparedStatement preparedStatement = connection.prepareStatement("UPDATE users SET isOnline = 0 WHERE userID = ?");

            preparedStatement.setString(1, userID);

            preparedStatement.executeUpdate();

            connection.close();

            return;
        } catch (Exception e) {
            System.out.println(e.getMessage());
            return;
        }
    }

}
