package com.example.dbmanager;

import java.sql.*;
import java.util.ArrayList;

public class Read {
    private Connection connection;
    private String dbName;

    Read(Connection connection, String dbName) {
        this.connection = connection;
        this.dbName = dbName;
    }

    public void useDB(String dbName) throws SQLException {
        connection.createStatement().execute(String.format("use %s", dbName));
    }

    public ArrayList<String> showDB() throws SQLException {
        // 쿼리 생성.
        Statement statement = connection.createStatement();
        ResultSet resultSet = statement.executeQuery("show databases");
        ArrayList<String> results = new ArrayList<String>();

        while (resultSet.next())
            results.add(resultSet.getString(1));
        return results;
    }

    public ArrayList<String> showTables() throws SQLException {
        // 쿼리 생성.
        Statement statement = connection.createStatement();
        ResultSet resultSet = statement.executeQuery(String.format("show tables from %s", dbName));
        ArrayList<String> results = new ArrayList<String>();
        
        while (resultSet.next())
            results.add(resultSet.getString(1));
        return results;
    }

    public ArrayList<ArrayList<String>> selectFrom(String tableName, String[] resultColumnNames, String[] columnNames, String[] conditions) throws SQLException {
        // 쿼리 생성.
        Statement statement = connection.createStatement();
        String query = String.format("select * from %s", tableName);
        int startIndex = 2;

        if (resultColumnNames != null) {
            String replaceColumnNames = String.format("%s", resultColumnNames[0]);
            for (int i = 1; i < resultColumnNames.length; i++)
                replaceColumnNames += String.format(", ", resultColumnNames[i]);
            query = query.replace("*", replaceColumnNames);
            startIndex = 1;
        }

        if (columnNames != null) {
            query += " where";
            for (int i = 0; i < columnNames.length; i++)
                query += String.format(" %s = %s", columnNames[i], conditions[i]);
        }

        ResultSet resultSet = statement.executeQuery(query);

        ArrayList<ArrayList<String>> results = new ArrayList<ArrayList<String>>();
        int columnLength = resultSet.getMetaData().getColumnCount();

        ArrayList<String> temp = new ArrayList<String>();
        for (int i = startIndex; i <= columnLength; i++)
            temp.add(resultSet.getMetaData().getColumnName(i));
        results.add(temp);

        while (resultSet.next()) {
            ArrayList<String> result = new ArrayList<String>();
            for (int i = startIndex; i <= columnLength; i++)
                result.add(resultSet.getString(i));
            results.add(result);
        }

        return results;
    }
}