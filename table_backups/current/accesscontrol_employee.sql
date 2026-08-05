-- Table: accesscontrol_employee
-- Mode: IN-PLACE
-- Backup Date: 2026-02-26 15:49:47
-- Row Count: 27
-- Hash: 16b5482788fef9bacff4f69d1a95acaa

DROP TABLE IF EXISTS accesscontrol_employee;
CREATE TABLE "accesscontrol_employee" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_name" varchar(200) NOT NULL, "can_view" bool NOT NULL, "can_add" bool NOT NULL, "can_edit" bool NOT NULL, "can_delete" bool NOT NULL, "can_export" bool NOT NULL, "employee_id" bigint NOT NULL REFERENCES "employees" ("id") DEFERRABLE INITIALLY DEFERRED);

INSERT INTO accesscontrol_employee VALUES (1, 'Customer', 1, 1, 1, 1, 1, 1);
INSERT INTO accesscontrol_employee VALUES (2, 'Employee', 1, 1, 1, 1, 1, 1);
INSERT INTO accesscontrol_employee VALUES (3, 'Role', 1, 1, 1, 1, 1, 1);
INSERT INTO accesscontrol_employee VALUES (4, 'Location', 1, 1, 1, 1, 1, 1);
INSERT INTO accesscontrol_employee VALUES (5, 'Project', 1, 1, 1, 1, 1, 1);
INSERT INTO accesscontrol_employee VALUES (6, 'Version', 1, 1, 1, 1, 1, 1);
INSERT INTO accesscontrol_employee VALUES (7, 'ContactUs', 1, 1, 1, 1, 1, 1);
INSERT INTO accesscontrol_employee VALUES (8, 'Coordination_and_Execution_Escalation', 1, 1, 1, 1, 1, 1);
INSERT INTO accesscontrol_employee VALUES (9, 'Customer', 1, 1, 1, 0, 1, 3);
INSERT INTO accesscontrol_employee VALUES (10, 'Employee', 1, 1, 1, 0, 1, 3);
INSERT INTO accesscontrol_employee VALUES (11, 'Project', 1, 1, 1, 0, 1, 5);
INSERT INTO accesscontrol_employee VALUES (12, 'Version', 1, 1, 1, 0, 1, 5);
INSERT INTO accesscontrol_employee VALUES (13, 'ContactUs', 1, 1, 1, 0, 1, 7);
INSERT INTO accesscontrol_employee VALUES (14, 'Coordination_and_Execution_Escalation', 1, 1, 1, 0, 1, 7);
INSERT INTO accesscontrol_employee VALUES (15, 'Customer', 1, 1, 1, 1, 1, 4);
INSERT INTO accesscontrol_employee VALUES (16, 'Employee', 1, 1, 1, 0, 1, 4);
INSERT INTO accesscontrol_employee VALUES (17, 'Role', 1, 1, 1, 1, 1, 4);
INSERT INTO accesscontrol_employee VALUES (18, 'Location', 1, 1, 1, 1, 1, 4);
INSERT INTO accesscontrol_employee VALUES (19, 'Project', 1, 1, 1, 1, 1, 4);
INSERT INTO accesscontrol_employee VALUES (20, 'Version', 1, 1, 1, 1, 1, 4);
INSERT INTO accesscontrol_employee VALUES (21, 'ContactUs', 1, 1, 1, 1, 1, 4);
INSERT INTO accesscontrol_employee VALUES (22, 'Coordination_and_Execution_Escalation', 1, 1, 1, 1, 1, 4);
INSERT INTO accesscontrol_employee VALUES (25, 'AccessControl_Role', 1, 1, 1, 1, 1, 1);
INSERT INTO accesscontrol_employee VALUES (26, 'AccessControl_Employee', 1, 1, 1, 1, 1, 1);
INSERT INTO accesscontrol_employee VALUES (27, 'Changedetails', 1, 1, 1, 1, 1, 1);
INSERT INTO accesscontrol_employee VALUES (28, 'Remedy2Hippo', 1, 1, 1, 1, 1, 1);
INSERT INTO accesscontrol_employee VALUES (29, 'task_information', 1, 1, 1, 1, 1, 1);
