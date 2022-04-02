package com.example.dbmanager;

import java.sql.*;

public class Delete {
    private Connection connection;

    public Delete(Connection connection) {
        this.connection = connection;
    }

    public boolean dropDB(String dbName) throws SQLException {
        // 쿼리 생성.
        Statement statement = connection.createStatement();
        String query = String.format("drop database %s", dbName);

        try {
            statement.execute(query);
        } catch (SQLException e) {
            System.out.printf("[Failed] Failed to drop database '%s'.%n", dbName);
            System.out.println("\t" + e.toString());
            return false;
        }

        return true;
    }

    public boolean dropTabel(String tableName) throws SQLException {
        // 쿼리 생성.
        Statement statement = connection.createStatement();
        String query = String.format("drop table %s", tableName);

        try {
            statement.execute(query);
        } catch (SQLException e) {
            System.out.printf("[Failed] Failed to drop table '%s'.%n", tableName);
            System.out.println("\t" + e.toString());
            return false;
        }

        return true;
    }

    public boolean dropColumn(String tableName, String columnName) throws SQLException {
        // 쿼리 생성.
        Statement statement = connection.createStatement();
        String query = String.format("alter table %s drop column %s", tableName, columnName);

        try {
            statement.execute(query);
        } catch (SQLException e) {
            System.out.printf("[Failed] Failed to drop column '%s' from %s.%n", columnName, tableName);
            System.out.println("\t" + e.toString());
            return false;
        }

        return true;
    }

    public boolean delete(String tableName, String[] columnNames, String[] conditions) throws SQLException {
        // 쿼리 생성.
        Statement statement = connection.createStatement();
        String query = String.format("delete from %s", tableName);

        if (columnNames != null) {
            query += " where";
            for (int i = 0; i < columnNames.length; i++)
                query += String.format(" %s = %s", columnNames[i], conditions[i]);
        }

        try {
            statement.execute(query);
        } catch (SQLException e) {
            System.out.printf("[Failed] Failed to delete from '%s'.%n", tableName);
            System.out.println("\t" + e.toString());
            return false;
        }

        return true;
    }
}