-- Table: crq_properties
-- Mode: IN-PLACE
-- Backup Date: 2026-05-14 09:23:00
-- Row Count: 6
-- Hash: af446b589022f706a9afba1592239056

DROP TABLE IF EXISTS crq_properties;
CREATE TABLE "crq_properties" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "is_impacting" bool NOT NULL, "change_type" varchar(100) NOT NULL, "manager_group" varchar(100) NOT NULL, "class" varchar(100) NOT NULL, "impact" varchar(100) NOT NULL, "urgency" varchar(100) NOT NULL, "risk_level" varchar(100) NOT NULL, "estimated_outage_duration" varchar(100) NOT NULL, "operational_categorization_1" varchar(100) NOT NULL, "operational_categorization_2" varchar(100) NOT NULL, "service_impact_assessment_work_info" text NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);

INSERT INTO crq_properties VALUES (1, 1, 'Service / Normal Maintenance', 'Infra Change', 'No Impact', '2-Significant/Large', '4-Low', 'Risk Level 3', '1 hour to 6 hours', 'IT', 'Internal', 'System health checks have been performed via environment audits and no redundancy and resiliency assessment is required for localised agent upgrades', '2026-05-13 08:38:19.256265', '2026-05-13 08:48:31.792452');
INSERT INTO crq_properties VALUES (2, 1, 'Customer Change', 'Client Change', 'Standard', '2-Significant/Large', '4-Low', 'Risk Level 3', '1 hour to 4 hours', 'Hosting', 'OS Patch/Agent Upgrade', '', '2026-05-13 08:50:38.374159', '2026-05-13 08:50:38.374183');
INSERT INTO crq_properties VALUES (3, 1, 'Emergency Maintenance', 'Infra Change', 'Emergency', '1-Extensive/Widespread', '2-High', 'Risk Level 1', '1 hour to 4 hours', 'Hosting', 'Hosting Network Services', 'System health checks have been performed via environment audits and no redundancy and resiliency assessment is required for localised agent upgrades', '2026-05-13 08:51:25.281008', '2026-05-13 08:51:25.281032');
INSERT INTO crq_properties VALUES (4, 0, 'Service / Normal Maintenance', 'Infra Change', 'No Impact', '4-Minor/Localized', '4-Low', 'Risk Level 3', '1 hour to 2 hours', 'IT', 'Internal', 'System health checks have been performed via environment audits and no kernel upgrade or reboot will occur', '2026-05-13 08:52:59.253337', '2026-05-13 08:52:59.253375');
INSERT INTO crq_properties VALUES (5, 0, 'Customer Change', 'Client Change', 'Standard', '4-Minor/Localized', '4-Low', 'Risk Level 3', 'No Disruption (Default)', 'Customer', 'OS Patch/Agent Upgrade', '', '2026-05-13 08:53:32.097641', '2026-05-13 08:53:32.097837');
INSERT INTO crq_properties VALUES (6, 0, 'Emergency Maintenance', 'Infra Change', 'Emergency', '1-Extensive/Widespread', '2-High', 'Risk Level 3', 'No Disruption (Default)', 'Hosting', 'Hosting Network Services', 'System health checks have been performed via environment audits and no redundancy and resiliency assessment is required for localised agent upgrades', '2026-05-13 08:54:05.460591', '2026-05-13 08:54:05.460623');
