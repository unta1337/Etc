package com.example.dbmanager;

import java.sql.*;

public class Create {
    private Connection connection;

    Create(Connection connection) {
        this.connection = connection;
    }

    public boolean createDB(String dbName) throws SQLException {
        // DB가 이미 존재하면 생성하지 않음.
        if (connection.createStatement().executeQuery(String.format("show databases like '%s'", dbName)).next()) {
            System.out.printf("[Failed] Database '%s' alreay exist.%n", dbName);
            return false;
        }

        String query = String.format("create database %s", dbName);
        Statement statement = connection.createStatement();
        statement.execute(query);
        return true;
    }

    public boolean createTable(String tableName) throws SQLException {
        // table이 이미 존재하면 생성하지 않음.
        if (connection.createStatement().executeQuery(String.format("show tables like '%s'", tableName)).next()) {
            System.out.printf("[Failed] Table '%s' already exist.%n", tableName);
            return false;
        }

        String query = String.format("create table %s (__dummy int)", tableName);
        Statement statement = connection.createStatement();
        statement.execute(query);
        return true;
    }

    public boolean addColumn(String tableName, String columnName, String type, String[] constraints) throws SQLException {
        // column이 이미 존재하면 생성하지 않음.
        if (connection.createStatement().executeQuery(String.format("show columns from %s like '%s'", tableName, columnName)).next()) {
            System.out.printf("[Failed] Column '%s' already exist.%n", columnName);
            return false;
        }

        String query = String.format("alter table %s add column %s %s", tableName, columnName, type);
        if (constraints != null)
            for (String constraint : constraints)
                query += " " + constraint;
        Statement statement = connection.createStatement();
        statement.execute(query);
        return true;
    }

    public boolean insertInto(String tableName, String[] columnNames, String[] values) throws SQLException {
        // 주어진 쿼리의 파라미터 삽입.
        String query = String.format("insert into %s (%s", tableName, columnNames[0]);
        for (int i = 1; i < columnNames.length; i++) query += ", " + columnNames[i];
        query += ") values (" + values[0];
        for (int i = 1; i < values.length; i++) query += ", " + values[i];
        query += ")";
        Statement statement = connection.createStatement();

        try {
            statement.execute(query);
        } catch (SQLException e) {
            System.out.printf("[Failed] Failed to insert into table '%s'.%n", tableName);
            System.out.println("\t" + e.toString());
            return false;
        }
        return true;
    }
}