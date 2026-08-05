-- Table: coordination_and_execution_escalations_employees
-- Mode: IN-PLACE
-- Backup Date: 2026-06-24 06:58:51
-- Row Count: 6
-- Hash: 1a0de79988114cd44e26efd3aa6c73a0

DROP TABLE IF EXISTS coordination_and_execution_escalations_employees;
CREATE TABLE "coordination_and_execution_escalations_employees" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "coordinationandexecutionescalation_id" bigint NOT NULL REFERENCES "coordination_and_execution_escalations" ("id") DEFERRABLE INITIALLY DEFERRED, "employee_id" bigint NOT NULL REFERENCES "employees" ("id") DEFERRABLE INITIALLY DEFERRED);

INSERT INTO coordination_and_execution_escalations_employees VALUES (1, 1, 3);
INSERT INTO coordination_and_execution_escalations_employees VALUES (3, 2, 6);
INSERT INTO coordination_and_execution_escalations_employees VALUES (4, 3, 2);
INSERT INTO coordination_and_execution_escalations_employees VALUES (5, 4, 19);
INSERT INTO coordination_and_execution_escalations_employees VALUES (6, 1, 10);
INSERT INTO coordination_and_execution_escalations_employees VALUES (7, 1, 13);
