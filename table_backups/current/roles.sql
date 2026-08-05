-- Table: roles
-- Mode: IN-PLACE
-- Backup Date: 2026-02-16 11:55:38
-- Row Count: 5
-- Hash: a768ce4865a34de375523ae6d778c22a

DROP TABLE IF EXISTS roles;
CREATE TABLE "roles" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL UNIQUE, "description" text NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, CONSTRAINT "unique_role_name" UNIQUE ("name"));

INSERT INTO roles VALUES (1, 'Manager', 'Lead and motivate teams to achieve organizational goals with vision and guidance.

Plan and make decisions by setting objectives, allocating resources, and strategizing effectively.

Communicate and coordinate across teams and stakeholders to ensure clarity and collaboration.

Monitor performance and develop people through feedback, coaching, and continuous improvement.', '2025-11-03 10:58:38.484240', '2025-12-17 09:02:02.981938');
INSERT INTO roles VALUES (2, 'Release Manager', 'Oversees and ensures the effective coordination of the entire change process

Responsible for customer communications, release schedule management, and leading change initiatives

Manage change success and remediation

Monitor risks and ensure compliance to maintain stability and quality', '2025-11-03 11:32:43.867200', '2025-12-17 09:03:53.945633');
INSERT INTO roles VALUES (3, 'Release Engineer', 'Perform upfront validation

Responsible for writing MOPs (Methods of Procedure)

Responsible for change execution

Manage and evaluate change outcomes', '2025-11-03 11:33:04.626766', '2025-12-17 09:03:27.660951');
INSERT INTO roles VALUES (4, 'Developer', 'Own the development and implementation of automated methodologies.

Engineer solutions through pilot

Provide early life support

Continuously optimize and scale solutions for sustained efficiency and improvement', '2025-11-03 11:29:12.912985', '2025-12-17 09:02:39.177150');
INSERT INTO roles VALUES (5, 'Admin', '', '2025-11-19 04:35:33.703003', '2025-11-19 04:35:33.703041');
