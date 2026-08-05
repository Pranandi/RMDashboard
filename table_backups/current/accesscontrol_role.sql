-- Table: accesscontrol_role
-- Mode: IN-PLACE
-- Backup Date: 2026-05-13 10:44:06
-- Row Count: 58
-- Hash: 83d38905fcdfbd45a9f13ed3123831bc

DROP TABLE IF EXISTS accesscontrol_role;
CREATE TABLE "accesscontrol_role" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "can_view" bool NOT NULL, "can_add" bool NOT NULL, "can_edit" bool NOT NULL, "can_delete" bool NOT NULL, "can_export" bool NOT NULL, "role_id" bigint NOT NULL REFERENCES "roles" ("id") DEFERRABLE INITIALLY DEFERRED, "app_name" varchar(200) NOT NULL);

INSERT INTO accesscontrol_role VALUES (1, 1, 1, 1, 1, 1, 1, 'Customer');
INSERT INTO accesscontrol_role VALUES (2, 1, 1, 1, 1, 1, 1, 'Employee');
INSERT INTO accesscontrol_role VALUES (3, 1, 1, 1, 1, 1, 1, 'Role');
INSERT INTO accesscontrol_role VALUES (4, 1, 1, 1, 1, 1, 1, 'Location');
INSERT INTO accesscontrol_role VALUES (5, 1, 1, 1, 1, 1, 1, 'Project');
INSERT INTO accesscontrol_role VALUES (6, 1, 1, 1, 1, 1, 1, 'Version');
INSERT INTO accesscontrol_role VALUES (7, 1, 1, 1, 1, 1, 1, 'ContactUs');
INSERT INTO accesscontrol_role VALUES (8, 1, 1, 1, 1, 1, 1, 'Coordination_and_Execution_Escalation');
INSERT INTO accesscontrol_role VALUES (9, 1, 0, 0, 0, 0, 2, 'Employee');
INSERT INTO accesscontrol_role VALUES (10, 1, 0, 0, 0, 1, 2, 'Role');
INSERT INTO accesscontrol_role VALUES (11, 1, 0, 0, 0, 1, 2, 'Location');
INSERT INTO accesscontrol_role VALUES (12, 1, 1, 1, 0, 1, 2, 'Project');
INSERT INTO accesscontrol_role VALUES (13, 1, 1, 1, 1, 1, 2, 'Version');
INSERT INTO accesscontrol_role VALUES (14, 1, 0, 0, 0, 1, 2, 'ContactUs');
INSERT INTO accesscontrol_role VALUES (15, 1, 0, 0, 0, 1, 2, 'Coordination_and_Execution_Escalation');
INSERT INTO accesscontrol_role VALUES (16, 1, 1, 0, 1, 1, 4, 'Customer');
INSERT INTO accesscontrol_role VALUES (17, 1, 0, 0, 0, 1, 4, 'Employee');
INSERT INTO accesscontrol_role VALUES (18, 1, 0, 0, 0, 1, 4, 'Role');
INSERT INTO accesscontrol_role VALUES (19, 1, 0, 0, 0, 1, 4, 'Location');
INSERT INTO accesscontrol_role VALUES (20, 1, 0, 0, 0, 1, 4, 'Project');
INSERT INTO accesscontrol_role VALUES (21, 1, 0, 0, 0, 1, 4, 'Version');
INSERT INTO accesscontrol_role VALUES (22, 1, 1, 1, 0, 1, 4, 'ContactUs');
INSERT INTO accesscontrol_role VALUES (23, 1, 1, 1, 0, 1, 4, 'Coordination_and_Execution_Escalation');
INSERT INTO accesscontrol_role VALUES (24, 1, 1, 1, 1, 1, 3, 'Customer');
INSERT INTO accesscontrol_role VALUES (25, 1, 0, 0, 0, 1, 3, 'Employee');
INSERT INTO accesscontrol_role VALUES (26, 1, 0, 0, 0, 1, 3, 'Role');
INSERT INTO accesscontrol_role VALUES (27, 1, 0, 0, 0, 1, 3, 'Location');
INSERT INTO accesscontrol_role VALUES (28, 1, 0, 0, 0, 1, 3, 'Project');
INSERT INTO accesscontrol_role VALUES (29, 1, 0, 0, 0, 1, 3, 'Version');
INSERT INTO accesscontrol_role VALUES (30, 1, 0, 0, 0, 1, 3, 'ContactUs');
INSERT INTO accesscontrol_role VALUES (31, 1, 0, 0, 0, 1, 3, 'Coordination_and_Execution_Escalation');
INSERT INTO accesscontrol_role VALUES (32, 1, 1, 1, 1, 1, 1, 'AccessControl_Role');
INSERT INTO accesscontrol_role VALUES (33, 1, 1, 1, 1, 1, 1, 'AccessControl_Employee');
INSERT INTO accesscontrol_role VALUES (34, 1, 0, 0, 0, 0, 4, 'AccessControl_Role');
INSERT INTO accesscontrol_role VALUES (35, 1, 0, 0, 0, 0, 4, 'AccessControl_Employee');
INSERT INTO accesscontrol_role VALUES (36, 1, 1, 1, 0, 1, 5, 'Employee');
INSERT INTO accesscontrol_role VALUES (37, 1, 0, 0, 0, 1, 5, 'Role');
INSERT INTO accesscontrol_role VALUES (38, 1, 0, 0, 0, 1, 5, 'Location');
INSERT INTO accesscontrol_role VALUES (39, 1, 0, 0, 0, 1, 5, 'Customer');
INSERT INTO accesscontrol_role VALUES (40, 1, 0, 0, 0, 1, 5, 'Project');
INSERT INTO accesscontrol_role VALUES (41, 1, 0, 0, 0, 1, 5, 'Version');
INSERT INTO accesscontrol_role VALUES (42, 1, 0, 0, 0, 1, 5, 'Coordination_and_Execution_Escalation');
INSERT INTO accesscontrol_role VALUES (43, 1, 0, 0, 0, 1, 5, 'ContactUs');
INSERT INTO accesscontrol_role VALUES (44, 1, 0, 0, 0, 1, 5, 'AccessControl_Role');
INSERT INTO accesscontrol_role VALUES (45, 1, 0, 0, 0, 1, 5, 'AccessControl_Employee');
INSERT INTO accesscontrol_role VALUES (46, 1, 1, 1, 1, 1, 4, 'Changedetails');
INSERT INTO accesscontrol_role VALUES (47, 1, 1, 1, 1, 1, 4, 'Remedy2Hippo');
INSERT INTO accesscontrol_role VALUES (48, 1, 1, 1, 1, 1, 4, 'task_information');
INSERT INTO accesscontrol_role VALUES (49, 1, 1, 1, 1, 1, 4, 'clients');
INSERT INTO accesscontrol_role VALUES (50, 1, 1, 1, 1, 1, 4, 'crq_client_approval');
INSERT INTO accesscontrol_role VALUES (51, 1, 1, 1, 1, 1, 4, 'crq_coordination');
INSERT INTO accesscontrol_role VALUES (52, 1, 1, 1, 1, 1, 4, 'crq_additional_tasks');
INSERT INTO accesscontrol_role VALUES (53, 1, 1, 1, 1, 1, 4, 'crq_properties');
INSERT INTO accesscontrol_role VALUES (54, 1, 1, 1, 1, 1, 4, 'dc_region');
INSERT INTO accesscontrol_role VALUES (55, 1, 0, 0, 0, 1, 4, 'uploader_projects');
INSERT INTO accesscontrol_role VALUES (56, 1, 0, 0, 0, 1, 4, 'uploader_variants');
INSERT INTO accesscontrol_role VALUES (57, 1, 1, 1, 1, 1, 4, 'timezone_table');
INSERT INTO accesscontrol_role VALUES (58, 1, 1, 1, 1, 1, 4, 'aip_data');
