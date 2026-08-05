-- Table: locations
-- Mode: IN-PLACE
-- Backup Date: 2026-02-16 11:55:38
-- Row Count: 4
-- Hash: f734563eb0f51c149dc0628cb8434823

DROP TABLE IF EXISTS locations;
CREATE TABLE "locations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "address" text NOT NULL, "working_hours" varchar(100) NOT NULL, "timezone" varchar(50) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "role_id" bigint NULL REFERENCES "roles" ("id") DEFERRABLE INITIALLY DEFERRED, "working_days" varchar(100) NOT NULL);

INSERT INTO locations VALUES (1, 'India', 'Bengaluru', '09:00 - 18:00', 'Asia/Calcutta', '2025-11-03 10:59:13.345591', '2025-11-03 11:35:17.529561', 1, 'Monday-Friday');
INSERT INTO locations VALUES (2, 'India', 'Bangaluru', '06:00 - 21:00', 'Asia/Calcutta', '2025-11-03 11:35:55.648365', '2025-12-17 07:45:43.510777', 2, 'Monday-Friday');
INSERT INTO locations VALUES (3, 'India', 'Bangaluru', '00:00 - 23:59', 'Asia/Calcutta', '2025-11-03 11:36:18.425276', '2025-11-03 11:36:18.425338', 3, 'All Days');
INSERT INTO locations VALUES (4, 'India', 'Bangaluru', '09:00 - 18:00', 'Asia/Calcutta', '2025-11-03 11:35:05.294484', '2025-11-03 11:35:05.294527', 4, 'Monday-Friday');
