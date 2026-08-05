-- Table: django_admin_log
-- Mode: IN-PLACE
-- Backup Date: 2025-11-17 17:10:59
-- Row Count: 0
-- Hash: c921b332eb2e07149e033d32a616b366

DROP TABLE IF EXISTS django_admin_log;
CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_time" datetime NOT NULL);

