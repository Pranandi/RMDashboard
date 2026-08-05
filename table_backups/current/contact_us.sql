-- Table: contact_us
-- Mode: IN-PLACE
-- Backup Date: 2026-02-16 11:55:38
-- Row Count: 4
-- Hash: 152c0d028461f2bf3279ec90511cae8b

DROP TABLE IF EXISTS contact_us;
CREATE TABLE "contact_us" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "email" varchar(254) NOT NULL, "phone" varchar(15) NULL, "alternative_phone" varchar(15) NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "name" varchar(100) NOT NULL);

INSERT INTO contact_us VALUES (1, 'Release Management Manager', 'Satheesh.Lal@Lumen.com', '+919008022550', '', '2025-12-10 05:15:59.910130', '2025-12-18 06:50:59.122753', 'Satheesh Lal');
INSERT INTO contact_us VALUES (2, 'Director', 'ravi.rao@lumen.com', '+919845668271', '', '2025-12-10 05:16:46.418774', '2025-12-18 07:35:48.870552', 'Ravi Rao');
INSERT INTO contact_us VALUES (3, 'Senior Director', 'jeash.velayudhan@lumen.com', '+919880342834', '', '2025-12-10 05:17:42.169635', '2025-12-10 05:17:42.169651', 'Jeash Velayudhan');
INSERT INTO contact_us VALUES (4, 'Sr Dir Process Improvement', 'jeff.hessenflow@lumen.com', '+16367342462', '+1636237669', '2025-12-10 05:18:32.892500', '2025-12-17 05:06:01.852907', 'Jeff Hessenflow');
