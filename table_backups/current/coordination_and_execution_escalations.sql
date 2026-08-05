-- Table: coordination_and_execution_escalations
-- Mode: IN-PLACE
-- Backup Date: 2026-02-16 11:55:38
-- Row Count: 4
-- Hash: bb78812b46f48a6b3f8204e500d1f7df

DROP TABLE IF EXISTS coordination_and_execution_escalations;
CREATE TABLE "coordination_and_execution_escalations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "level" integer NOT NULL UNIQUE, "description" varchar(255) NOT NULL, "contact_type" varchar(50) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "location_id" bigint NOT NULL REFERENCES "locations" ("id") DEFERRABLE INITIALLY DEFERRED);

INSERT INTO coordination_and_execution_escalations VALUES (1, 1, 'Release Managers', 'Email,Teams,Phone', '2025-12-10 04:50:40.053433', '2025-12-22 05:13:29.526798', 1);
INSERT INTO coordination_and_execution_escalations VALUES (2, 2, 'Release Management Execution Team', 'Email', '2025-12-10 05:06:49.431724', '2025-12-22 05:14:04.472432', 1);
INSERT INTO coordination_and_execution_escalations VALUES (3, 3, 'Release Management - Manager', 'Email,Teams,Phone', '2025-12-10 05:07:21.348527', '2025-12-18 06:50:19.395138', 1);
INSERT INTO coordination_and_execution_escalations VALUES (4, 4, 'Coordination and Execution - Director', 'Email,Teams,Phone', '2025-12-17 05:35:02.804137', '2025-12-22 05:14:22.367794', 1);
