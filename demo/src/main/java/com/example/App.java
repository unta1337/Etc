package com.example;

import java.sql.*;

import com.example.dbmanager.DBManager;

public class App {
    public static void main(String[] args) throws ClassNotFoundException, SQLException {
        // DB 정보 정의.
        String dbURL = "jdbc:mysql://ksy.abstr.net:2801";
        String dbUser = "root";
        String dbPassword = "";

        // DB 내용 정의.
        String dbName = "community_database";
        String[] tableNames = { "user", "post", "comment", "hashtag", "post_hashtag_relation" };

        // user
        String[] userColumn = { "id_uniq", "id", "passwd", "member_since", "is_active", "num_warn" };
        String[] userType = { "int", "varchar(20)", "varchar(20)", "date", "tinyint", "int" };
        String[][] userConstraints = {
            { "not null", "primary key" },
            { "not null" },
            { "not null" },
            { "default curdate()" },
            { "default 0" },
            { "default 0" }
        };

        // post
        String[] postColumn = { "id", "title", "content", "author", "time_posted", "num_view", "num_like", "num_dislike" };
        String[] postType = { "int", "varchar(255)", "text", "int", "datetime", "int", "int", "int" };
        String[][] postConstraints = {
            { "not null", "primary key" },
            { "not null" },
            { "not null" },
            null,
            { "default current_timestamp()" },
            { "default 0" },
            { "default 0" },
            { "default 0" }
        };
        String[][] postForeignKeys = {
            { tableNames[1], postColumn[3], tableNames[0], userColumn[0] }
        };
        String[][] postFKConstraints = {
            { "on update cascade", "on delete set null" }
        };

        // comment
        String[] commentColumn = { "id", "comment", "author", "time_posted", "post_id" };
        String[] commentType = { "int", "text", "int", "datetime", "int" };
        String[][] commentConstraints = {
            { "not null", "primary key" },
            { "not null" },
            null,
            { "default current_timestamp()" },
            null
        };
        String[][] commentForeignKeys = {
            { tableNames[2], commentColumn[2], tableNames[0], userColumn[0] },
            { tableNames[2], commentColumn[4], tableNames[1], postColumn[0] }
        };
        String[][] commnetFKConstraints = {
            { "on update cascade", "on delete set null" },
            { "on update cascade", "on delete cascade" }
        };

        // hashtag
        String[] hashtagColumn = { "id", "tag" };
        String[] hashtagType = { "int", "varchar(20)" };
        String[][] hashtagConstraints = {
            { "not null", "primary key" },
            { "not null" }
        };

        // post_hashtag_relation
        String[] postHashtagRelationColumn = { "post_id", "tag_id" };
        String[] postHashTagRelationType = { "int", "int" };
        String[][] postHashTagRelationConstraints = {
            null,
            null
        };
        String[][] postHashtagRelationForeignKeys = {
            { tableNames[4], postHashtagRelationColumn[0], tableNames[1], postColumn[0] },
            { tableNames[4], postHashtagRelationColumn[1], tableNames[3], hashtagColumn[0] }
        };
        String[][] postHashtagRelationFKConstraints = {
            { "on update cascade", "on delete cascade" },
            { "on update cascade", "on delete cascade" }
        };

        // DB 생성 및 접속.
        DBManager db = new DBManager(dbURL, dbUser, dbPassword, dbName);

        // 테이블 생성.
        for (String tableName : tableNames) {
            db.create.createTable(tableName);
        }
        
        // 컬럼 생성.
        for (int i = 0; i < userColumn.length; i++)
            db.create.addColumn(tableNames[0], userColumn[i], userType[i], userConstraints[i]);
        for (int i = 0; i < postColumn.length; i++)
            db.create.addColumn(tableNames[1], postColumn[i], postType[i], postConstraints[i]);
        for (int i = 0; i < commentColumn.length; i++)
            db.create.addColumn(tableNames[2], commentColumn[i], commentType[i], commentConstraints[i]);
        for (int i = 0; i < hashtagColumn.length; i++)
            db.create.addColumn(tableNames[3], hashtagColumn[i], hashtagType[i], hashtagConstraints[i]);
        for (int i = 0; i < postHashtagRelationColumn.length; i++)
            db.create.addColumn(tableNames[4], postHashtagRelationColumn[i], postHashTagRelationType[i], postHashTagRelationConstraints[i]);
        
        // 외래키 설정.
        for (int i = 0; i < postForeignKeys.length; i++)
            db.update.setForeignKey(postForeignKeys[i][0], postForeignKeys[i][1], postForeignKeys[i][2], postForeignKeys[i][3], postFKConstraints[i]);
        for (int i = 0; i < commentForeignKeys.length; i++)
            db.update.setForeignKey(commentForeignKeys[i][0], commentForeignKeys[i][1], commentForeignKeys[i][2], commentForeignKeys[i][3], commnetFKConstraints[i]);
        for (int i = 0; i < postHashtagRelationForeignKeys.length; i++)
            db.update.setForeignKey(postHashtagRelationForeignKeys[i][0], postHashtagRelationForeignKeys[i][1], postHashtagRelationForeignKeys[i][2], postHashtagRelationForeignKeys[i][3], postHashtagRelationFKConstraints[i]);
    }
}