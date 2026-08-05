-- Table: auth_user_user_permissions
-- Mode: IN-PLACE
-- Backup Date: 2025-11-17 17:10:59
-- Row Count: 0
-- Hash: c449cbdf3009a7905a590d024df5b55b

DROP TABLE IF EXISTS auth_user_user_permissions;
CREATE TABLE "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);

