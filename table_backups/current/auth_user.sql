-- Table: auth_user
-- Mode: IN-PLACE
-- Backup Date: 2025-11-17 17:10:59
-- Row Count: 0
-- Hash: 741b17ed9b358652978910edd90cc686

DROP TABLE IF EXISTS auth_user;
CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "first_name" varchar(150) NOT NULL);

