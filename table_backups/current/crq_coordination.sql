-- Table: crq_coordination
-- Mode: IN-PLACE
-- Backup Date: 2026-05-14 09:23:00
-- Row Count: 4
-- Hash: 48b372dcb0b1a129904263db710934d9

DROP TABLE IF EXISTS crq_coordination;
CREATE TABLE "crq_coordination" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "coordination" varchar(100) NOT NULL, "coordinator_company" varchar(100) NOT NULL, "coordinator_organization" varchar(100) NOT NULL, "workgroup" varchar(100) NOT NULL, "change_coordinator" varchar(100) NOT NULL, "task_summary" text NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "task_name" varchar(100) NULL);

INSERT INTO crq_coordination VALUES (1, 'RM', 'Savvis', 'Operations', 'ReleaseMgmt', 'Satheesh Lal', 'Carry out steps in MOP', '2026-05-11 08:52:11.304603', '2026-05-11 08:52:43.611114', 'RM Task');
INSERT INTO crq_coordination VALUES (2, 'RM ZT', 'Savvis', 'Operations', 'ReleaseMgmt', 'Hippo Automation', '', '2026-05-13 08:13:47.600548', '2026-05-13 08:13:47.600607', NULL);
INSERT INTO crq_coordination VALUES (3, 'UNIX', 'Savvis', 'Operations', 'UNIX_T3', 'Default Operations', 'Carry out steps in MOP', '2026-05-13 08:14:27.933233', '2026-05-13 08:14:27.933301', 'Unix Task');
INSERT INTO crq_coordination VALUES (4, 'Windows', 'Savvis', 'Operations', 'Win_T3', 'Default Operations', 'Carry out steps in MOP', '2026-05-13 08:15:05.615132', '2026-05-13 08:15:19.403270', 'Windows Task');
