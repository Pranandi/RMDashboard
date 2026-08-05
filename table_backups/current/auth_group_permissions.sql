-- Table: auth_group_permissions
-- Mode: IN-PLACE
-- Backup Date: 2025-11-17 17:10:59
-- Row Count: 0
-- Hash: 49173ecc7f2de363185af8288f311f44

DROP TABLE IF EXISTS auth_group_permissions;
CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);

