-- Table: django_content_type
-- Mode: IN-PLACE
-- Backup Date: 2026-05-15 08:46:14
-- Row Count: 29
-- Hash: a7ca2a982aec63f2abc21ed2b4e66b57

DROP TABLE IF EXISTS django_content_type;
CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);

INSERT INTO django_content_type VALUES (1, 'admin', 'logentry');
INSERT INTO django_content_type VALUES (2, 'auth', 'permission');
INSERT INTO django_content_type VALUES (3, 'auth', 'group');
INSERT INTO django_content_type VALUES (4, 'auth', 'user');
INSERT INTO django_content_type VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO django_content_type VALUES (6, 'sessions', 'session');
INSERT INTO django_content_type VALUES (7, 'Role', 'role');
INSERT INTO django_content_type VALUES (8, 'Location', 'location');
INSERT INTO django_content_type VALUES (9, 'Employee', 'employee');
INSERT INTO django_content_type VALUES (10, 'Customer', 'customer');
INSERT INTO django_content_type VALUES (11, 'Project', 'project');
INSERT INTO django_content_type VALUES (12, 'Version', 'version');
INSERT INTO django_content_type VALUES (13, 'Coordination_and_Execution_Escalation', 'coordinationandexecutionescalation');
INSERT INTO django_content_type VALUES (14, 'ContactUs', 'contactus');
INSERT INTO django_content_type VALUES (15, 'AccessControl_Role', 'accesscontrol_role');
INSERT INTO django_content_type VALUES (16, 'AccessControl_Employee', 'accesscontrol_employee');
INSERT INTO django_content_type VALUES (17, 'Changedetails', 'changedetails');
INSERT INTO django_content_type VALUES (18, 'task_information', 'task_information');
INSERT INTO django_content_type VALUES (19, 'clients', 'clients');
INSERT INTO django_content_type VALUES (20, 'crq_additional_tasks', 'crqadditionaltask');
INSERT INTO django_content_type VALUES (21, 'crq_client_approval', 'crqclientapproval');
INSERT INTO django_content_type VALUES (22, 'crq_coordination', 'crqcoordination');
INSERT INTO django_content_type VALUES (23, 'crq_properties', 'crqproperties');
INSERT INTO django_content_type VALUES (24, 'dc_region', 'dcregion');
INSERT INTO django_content_type VALUES (25, 'uploader_projects', 'uploaderproject');
INSERT INTO django_content_type VALUES (26, 'uploader_variants', 'uploadervariant');
INSERT INTO django_content_type VALUES (27, 'timezone_table', 'timezonetable');
INSERT INTO django_content_type VALUES (28, 'aip_data', 'aipdata');
INSERT INTO django_content_type VALUES (29, 'server_details', 'serverdetails');
