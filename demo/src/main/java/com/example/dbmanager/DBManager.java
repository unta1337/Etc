package com.example.dbmanager;

import java.sql.*;

public class DBManager {
    // CURD 명령을 수행하는 객체를 갖는다.
    public Create create;
    public Read read;
    public Update update;
    public Delete delete;

    public DBManager(String url, String user, String password, String dbName) throws ClassNotFoundException, SQLException {
        String className = "com.mysql.cj.jdbc.Driver";
        Class.forName(className);

        // DBManager 내의 CRUD 객체는 모두 동일한 Connection을 갖는다.
        Connection connection = DriverManager.getConnection(url, user, password);

        this.create = new Create(connection);
        this.read = new Read(connection, dbName);
        this.update = new Update(connection);
        this.delete = new Delete(connection);

        this.create.createDB(dbName);
        this.read.useDB(dbName);
    }
}