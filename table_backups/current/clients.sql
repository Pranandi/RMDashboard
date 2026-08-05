-- Table: clients
-- Mode: IN-PLACE
-- Backup Date: 2026-05-14 09:23:00
-- Row Count: 6
-- Hash: 5fd30232e4af03b83609fa2be434fac8

DROP TABLE IF EXISTS clients;
CREATE TABLE "clients" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "client_name" varchar(100) NOT NULL, "vantive_name" varchar(100) NOT NULL, "site_id" varchar(100) NOT NULL, "advanced_essential" varchar(20) NOT NULL, "start_week" varchar(20) NOT NULL, "start_day" varchar(20) NOT NULL, "specific_date" date NULL, "frequency" varchar(20) NOT NULL, "notes" text NULL, "ask_for_approval_in_email" bool NOT NULL, "email_greeting" varchar(255) NULL, "email_to" varchar(255) NULL, "email_cc" varchar(255) NULL, "email_bcc" varchar(255) NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "is_active" bool NOT NULL, "add_month" varchar(20) NULL);

INSERT INTO clients VALUES (12, 'Savvis__Itential', 'Savvis', 'UNKNOWN', 'Essential', 'First', 'Monday', NULL, 'Quarterly', '', 0, NULL, 'David.Moore3@lumen.com,David.Stamper@lumen.com,Gurdyal.Singh@lumen.com,Jason.Patrick2@lumen.com,Seethalakshmi.Balachandran@lumen.com,ManagedServicesToolsApplicationSupport@centurylink.com,nick.havard@lumen.com', 'bruce.robertson@lumen.com', NULL, '2026-05-11 05:51:06.311683', '2026-05-11 07:57:20.366309', 1, NULL);
INSERT INTO clients VALUES (13, 'Savvis__HIE-Platform_PCI', 'Savvis', 'UNKNOWN', 'Essential', 'First', 'Monday', NULL, 'Monthly', '', 0, NULL, 'David.Moore3@lumen.com,David.Stamper@lumen.com,Gurdyal.Singh@lumen.com,Jason.Patrick2@lumen.com,Seethalakshmi.Balachandran@lumen.com,ManagedServicesToolsApplicationSupport@centurylink.com,nick.havard@lumen.com', 'bruce.robertson@lumen.com', NULL, '2026-05-11 05:51:06.311683', '2026-05-11 07:57:07.170991', 1, NULL);
INSERT INTO clients VALUES (14, 'Savvis__HPNA', 'Savvis', 'UNKNOWN', 'Essential', 'First', 'Monday', NULL, 'Quarterly', '', 0, NULL, NULL, NULL, NULL, '2026-05-11 05:51:06.311683', '2026-05-11 07:57:11.726182', 1, NULL);
INSERT INTO clients VALUES (15, 'Savvis__HPSA', 'Savvis', 'UNKNOWN', 'Essential', 'First', 'Monday', NULL, 'Quarterly', '', 0, NULL, NULL, NULL, NULL, '2026-05-11 05:51:06.311683', '2026-05-11 07:57:16.008108', 1, NULL);
INSERT INTO clients VALUES (16, 'Savvis__ActiveMQ', 'Savvis', 'UNKNOWN', 'Essential', 'First', 'Monday', NULL, 'Quarterly', '', 0, NULL, NULL, NULL, NULL, '2026-05-11 05:51:06.311683', '2026-05-11 07:56:56.954278', 1, NULL);
INSERT INTO clients VALUES (17, 'Savvis__OO', 'Savvis', 'UNKNOWN', 'Essential', 'First', 'Monday', NULL, 'Quarterly', '', 0, NULL, NULL, NULL, NULL, '2026-05-13 07:12:08.188354', '2026-05-13 07:12:08.188406', 1, NULL);
