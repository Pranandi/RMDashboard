-- Table: crq_client_approval
-- Mode: IN-PLACE
-- Backup Date: 2026-05-14 09:23:00
-- Row Count: 6
-- Hash: 012ead680e5534380b1ef784a65262c3

DROP TABLE IF EXISTS crq_client_approval;
CREATE TABLE "crq_client_approval" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "client_id" bigint NOT NULL REFERENCES "clients" ("id") DEFERRABLE INITIALLY DEFERRED, "approval_note" text NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "template_id" bigint NOT NULL REFERENCES "uploader_projects" ("id") DEFERRABLE INITIALLY DEFERRED);

INSERT INTO crq_client_approval VALUES (2, 12, 'RM: Standard Monthly OS Patching as agreed with Nick Havard', '2026-05-13 07:04:47.653988', '2026-05-13 07:04:47.654162', 24);
INSERT INTO crq_client_approval VALUES (3, 14, 'RM: Standard Monthly OS Patching as agreed with Sidhanti Sudheendra', '2026-05-13 07:10:03.265262', '2026-05-13 07:10:03.265315', 24);
INSERT INTO crq_client_approval VALUES (4, 15, 'RM: Standard Monthly OS Patching as agreed with Gurdyal Singh', '2026-05-13 07:10:30.576916', '2026-05-13 07:10:30.576970', 24);
INSERT INTO crq_client_approval VALUES (5, 16, 'RM: Standard Monthly OS Patching as agreed with David Stamper', '2026-05-13 07:10:45.642661', '2026-05-13 07:10:45.642726', 24);
INSERT INTO crq_client_approval VALUES (6, 13, 'RM: Standard Monthly OS Patching as agreed with HIE Platform Team', '2026-05-13 07:11:02.746533', '2026-05-13 07:11:02.746587', 24);
INSERT INTO crq_client_approval VALUES (7, 17, 'RM: Standard Monthly OS Patching as agreed with Seethalakshmi Balachandran', '2026-05-13 07:12:27.864948', '2026-05-13 07:12:27.864996', 24);
