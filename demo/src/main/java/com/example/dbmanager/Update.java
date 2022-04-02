package com.example.dbmanager;

import java.sql.*;

public class Update {
    private Connection connection;

    public Update(Connection connection) {
        this.connection = connection;
    }

    public boolean modifyColumn(String tableName, String columnName, String type, String[] constraints) throws SQLException {
        // column이 존재하지 않으면 변경 불가.
        if (!connection.createStatement().executeQuery(String.format("show columns from %s like '%s'", tableName, columnName)).next()) {
            System.out.printf("[Failed] Column '%s' does not exist.%n", columnName);
            return false;
        }

        String query = String.format("alter table %s modify column %s %s", tableName, columnName, type);
        if (constraints != null)
            for (String constraint : constraints)
                query += " " + constraint;
        Statement statement = connection.createStatement();
        statement.execute(query);
        return true;
    }

    public boolean setForeignKey(String tableName, String columnName, String refTableName, String refColumnName, String[] onFlags) throws SQLException {
        String query = String.format("alter table %s add foreign key (%s) references %s (%s)", tableName, columnName, refTableName, refColumnName);
        if (onFlags != null)
            for (String flag : onFlags)
                query += String.format(" %s", flag);
        Statement statement = connection.createStatement();

        try {
            statement.execute(query);
        } catch (SQLException e) {
            System.out.println("[Failed] Can not modify column to forien key.");
            System.out.println("\t" + e.toString());
            return false;
        }

        return true;
    }

    public boolean update(String tableName, String updateColumnName, String updateColumnValue, String[] columnNames, String[] conditions) throws SQLException {
        Statement statement = connection.createStatement();
        String query = String.format("update %s set %s = %s", tableName, updateColumnName, updateColumnValue);

        if (columnNames != null) {
            query += " where";
            for (int i = 0; i < columnNames.length; i++)
                query += String.format(" %s = %s", columnNames[i], conditions[i]);
        }

        try {
            statement.execute(query);
        } catch (SQLException e) {
            System.out.printf("[Failed] Failed to update '%s'.%n", tableName);
            System.out.println("\t" + e.toString());
            return false;
        }

        return true;
    }
}