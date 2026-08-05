-- Table: django_migrations
-- Mode: IN-PLACE
-- Backup Date: 2026-05-15 08:46:14
-- Row Count: 61
-- Hash: 3195ebafb5895d3f276b51ec16679e3e

DROP TABLE IF EXISTS django_migrations;
CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);

INSERT INTO django_migrations VALUES (1, 'Role', '0001_initial', '2026-03-02 08:59:38.713369');
INSERT INTO django_migrations VALUES (2, 'Location', '0001_initial', '2026-03-02 08:59:38.741907');
INSERT INTO django_migrations VALUES (3, 'Employee', '0001_initial', '2026-03-02 08:59:38.777984');
INSERT INTO django_migrations VALUES (4, 'AccessControl_Employee', '0001_initial', '2026-03-02 08:59:38.815627');
INSERT INTO django_migrations VALUES (5, 'AccessControl_Role', '0001_initial', '2026-03-02 08:59:38.855577');
INSERT INTO django_migrations VALUES (6, 'Changedetails', '0001_initial', '2026-03-02 08:59:38.887299');
INSERT INTO django_migrations VALUES (7, 'ContactUs', '0001_initial', '2026-03-02 08:59:38.918799');
INSERT INTO django_migrations VALUES (8, 'Coordination_and_Execution_Escalation', '0001_initial', '2026-03-02 08:59:38.965988');
INSERT INTO django_migrations VALUES (9, 'Customer', '0001_initial', '2026-03-02 08:59:39.002558');
INSERT INTO django_migrations VALUES (10, 'Project', '0001_initial', '2026-03-02 08:59:39.035411');
INSERT INTO django_migrations VALUES (11, 'Version', '0001_initial', '2026-03-02 08:59:39.078914');
INSERT INTO django_migrations VALUES (12, 'contenttypes', '0001_initial', '2026-03-02 08:59:39.109958');
INSERT INTO django_migrations VALUES (13, 'auth', '0001_initial', '2026-03-02 08:59:39.167142');
INSERT INTO django_migrations VALUES (14, 'admin', '0001_initial', '2026-03-02 08:59:39.201419');
INSERT INTO django_migrations VALUES (15, 'admin', '0002_logentry_remove_auto_add', '2026-03-02 08:59:39.248289');
INSERT INTO django_migrations VALUES (16, 'admin', '0003_logentry_add_action_flag_choices', '2026-03-02 08:59:39.275988');
INSERT INTO django_migrations VALUES (17, 'contenttypes', '0002_remove_content_type_name', '2026-03-02 08:59:39.365910');
INSERT INTO django_migrations VALUES (18, 'auth', '0002_alter_permission_name_max_length', '2026-03-02 08:59:39.425592');
INSERT INTO django_migrations VALUES (19, 'auth', '0003_alter_user_email_max_length', '2026-03-02 08:59:39.472775');
INSERT INTO django_migrations VALUES (20, 'auth', '0004_alter_user_username_opts', '2026-03-02 08:59:39.511159');
INSERT INTO django_migrations VALUES (21, 'auth', '0005_alter_user_last_login_null', '2026-03-02 08:59:39.551874');
INSERT INTO django_migrations VALUES (22, 'auth', '0006_require_contenttypes_0002', '2026-03-02 08:59:39.564312');
INSERT INTO django_migrations VALUES (23, 'auth', '0007_alter_validators_add_error_messages', '2026-03-02 08:59:39.591747');
INSERT INTO django_migrations VALUES (24, 'auth', '0008_alter_user_username_max_length', '2026-03-02 08:59:39.627815');
INSERT INTO django_migrations VALUES (25, 'auth', '0009_alter_user_last_name_max_length', '2026-03-02 08:59:39.665748');
INSERT INTO django_migrations VALUES (26, 'auth', '0010_alter_group_name_max_length', '2026-03-02 08:59:39.703575');
INSERT INTO django_migrations VALUES (27, 'auth', '0011_update_proxy_permissions', '2026-03-02 08:59:39.749930');
INSERT INTO django_migrations VALUES (28, 'auth', '0012_alter_user_first_name_max_length', '2026-03-02 08:59:39.786261');
INSERT INTO django_migrations VALUES (29, 'sessions', '0001_initial', '2026-03-02 08:59:39.818108');
INSERT INTO django_migrations VALUES (30, 'task_information', '0001_initial', '2026-03-02 08:59:39.850758');
INSERT INTO django_migrations VALUES (31, 'clients', '0001_initial', '2026-05-11 05:20:55.750878');
INSERT INTO django_migrations VALUES (32, 'clients', '0002_remove_clients_clients_active_28b49e_idx_and_more', '2026-05-11 05:30:43.855624');
INSERT INTO django_migrations VALUES (33, 'crq_additional_tasks', '0001_initial', '2026-05-11 07:32:47.341386');
INSERT INTO django_migrations VALUES (34, 'clients', '0003_alter_clients_add_month', '2026-05-11 07:56:51.879129');
INSERT INTO django_migrations VALUES (35, 'crq_additional_tasks', '0002_crqadditionaltask_created_at_and_more', '2026-05-11 08:33:03.211870');
INSERT INTO django_migrations VALUES (36, 'crq_client_approval', '0001_initial', '2026-05-11 08:33:03.248177');
INSERT INTO django_migrations VALUES (37, 'crq_client_approval', '0002_alter_crqclientapproval_timestamps', '2026-05-11 08:50:29.858606');
INSERT INTO django_migrations VALUES (38, 'crq_client_approval', '0002_alter_crqclientapproval_created_at_and_more', '2026-05-11 08:50:29.904073');
INSERT INTO django_migrations VALUES (39, 'crq_client_approval', '0003_merge_20260511_1420', '2026-05-11 08:50:29.936972');
INSERT INTO django_migrations VALUES (40, 'crq_coordination', '0001_initial', '2026-05-11 08:50:29.978802');
INSERT INTO django_migrations VALUES (41, 'crq_properties', '0001_initial', '2026-05-11 09:35:21.139887');
INSERT INTO django_migrations VALUES (42, 'crq_properties', '0002_rename_class__crqproperties_class1', '2026-05-11 09:35:21.202385');
INSERT INTO django_migrations VALUES (43, 'crq_client_approval', '0004_alter_crqclientapproval_client', '2026-05-11 10:16:55.107713');
INSERT INTO django_migrations VALUES (44, 'dc_region', '0001_initial', '2026-05-11 10:16:55.163505');
INSERT INTO django_migrations VALUES (45, 'aip_data', '0001_initial', '2026-05-11 11:06:02.653377');
INSERT INTO django_migrations VALUES (46, 'timezone_table', '0001_initial', '2026-05-11 11:06:02.713796');
INSERT INTO django_migrations VALUES (47, 'uploader_projects', '0001_initial', '2026-05-11 11:06:02.767128');
INSERT INTO django_migrations VALUES (48, 'uploader_variants', '0001_initial', '2026-05-11 11:06:02.821736');
INSERT INTO django_migrations VALUES (49, 'timezone_table', '0002_timezonetable_remedy_tz_dst_active_and_more', '2026-05-12 05:26:30.331736');
INSERT INTO django_migrations VALUES (50, 'crq_client_approval', '0005_alter_crqclientapproval_template', '2026-05-13 07:03:34.427616');
INSERT INTO django_migrations VALUES (51, 'crq_coordination', '0002_alter_crqcoordination_task_name', '2026-05-13 08:13:24.237735');
INSERT INTO django_migrations VALUES (52, 'crq_properties', '0003_alter_crqproperties_change_type_and_more', '2026-05-13 08:32:07.103270');
INSERT INTO django_migrations VALUES (53, 'crq_properties', '0002_alter_crqproperties_estimated_outage_duration', '2026-05-13 08:52:13.599414');
INSERT INTO django_migrations VALUES (54, 'server_details', '0001_initial', '2026-05-14 07:39:54.960295');
INSERT INTO django_migrations VALUES (55, 'server_details', '0002_alter_serverdetails_client', '2026-05-14 09:19:58.568861');
INSERT INTO django_migrations VALUES (56, 'server_details', '0003_alter_serverdetails_batch_alter_serverdetails_client_and_more', '2026-05-14 11:31:19.574421');
INSERT INTO django_migrations VALUES (57, 'server_details', '0004_alter_serverdetails_client', '2026-05-14 11:33:18.406844');
INSERT INTO django_migrations VALUES (58, 'server_details', '0005_alter_serverdetails_environment_and_more', '2026-05-14 11:54:13.735473');
INSERT INTO django_migrations VALUES (59, 'server_details', '0006_alter_serverdetails_server_type', '2026-05-14 11:57:05.584136');
INSERT INTO django_migrations VALUES (60, 'server_details', '0007_alter_serverdetails_application', '2026-05-14 11:57:05.642381');
INSERT INTO django_migrations VALUES (61, 'server_details', '0008_alter_serverdetails_operating_system', '2026-05-14 11:59:06.152469');
