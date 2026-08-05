-- Table: crq_additional_tasks
-- Mode: IN-PLACE
-- Backup Date: 2026-05-14 09:23:00
-- Row Count: 6
-- Hash: fc5db1104902647f397e447e71912ceb

DROP TABLE IF EXISTS crq_additional_tasks;
CREATE TABLE "crq_additional_tasks" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "task_name" varchar(100) NOT NULL, "summary" text NULL, "assignee" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);

INSERT INTO crq_additional_tasks VALUES (2, 'DB MSSQL Task', 'Carry out steps in MOP', 'Database_MSSQL', '2026-05-11 08:33:03.196254', '2026-05-11 08:33:03.203736');
INSERT INTO crq_additional_tasks VALUES (3, 'RM Task', 'Carry out steps in MOP', 'ReleaseMgmt', '2026-05-13 08:08:41.018124', '2026-05-13 08:08:41.018162');
INSERT INTO crq_additional_tasks VALUES (4, 'DB Oracle Task', 'Carry out steps in MOP', 'Database_OracleMySQL', '2026-05-13 08:09:03.490403', '2026-05-13 08:09:03.490441');
INSERT INTO crq_additional_tasks VALUES (5, 'Backup Task', 'Carry out steps in MOP', 'Backup', '2026-05-13 08:09:33.452392', '2026-05-13 08:09:33.452425');
INSERT INTO crq_additional_tasks VALUES (6, 'ADAPTIVE Unix Middleware', 'Carry out steps in MOP', 'ADAPTIVE_Unix_Middleware', '2026-05-13 08:09:49.769602', '2026-05-13 08:09:49.769656');
INSERT INTO crq_additional_tasks VALUES (7, 'IT Applications', 'Carry out steps in MOP', 'Applications', '2026-05-13 08:10:06.040126', '2026-05-13 08:10:06.040164');
