-- Table: auth_user_groups
-- Mode: IN-PLACE
-- Backup Date: 2025-11-17 17:10:59
-- Row Count: 0
-- Hash: 6eaeb195a49fe2a2294417c6bdb976ed

DROP TABLE IF EXISTS auth_user_groups;
CREATE TABLE "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);

