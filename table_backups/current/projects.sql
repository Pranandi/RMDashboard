-- Table: projects
-- Mode: IN-PLACE
-- Backup Date: 2026-02-16 11:55:38
-- Row Count: 4
-- Hash: f3d557434a94ba8b8b2fcea5729dfb12

DROP TABLE IF EXISTS projects;
CREATE TABLE "projects" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "description" text NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "code" varchar(3) NOT NULL UNIQUE, CONSTRAINT "unique_project_code" UNIQUE ("code"));

INSERT INTO projects VALUES (1, 'Netbackup Upgrade', 'The NetBackup Client Upgrade Programme is designed to ensure all NetBackup Clients are upgraded to the latest version supported by the back-end NetBackup Master Servers. This upgrade enhances compatibility, improves performance, and strengthens reliability across the backup environment, while maintaining seamless integration with existing infrastructure.', '2025-11-03 14:07:21.438017', '2025-11-24 06:23:15.903546', '55');
INSERT INTO projects VALUES (2, 'VMTools Upgrade', 'This project focuses on upgrading VMware Tools to the latest version supported by both the Guest Operating System and the underlying ESX/ESXi host. The upgrade ensures improved compatibility, performance, and stability across virtual machines, while enabling seamless integration with the virtualization platform.', '2025-11-20 05:11:41.618098', '2025-12-01 05:38:15.963579', '76');
INSERT INTO projects VALUES (3, 'McAfee ENS and Agent Upgrade', 'This project aims to upgrade the existing McAfee VirusScan Engine to McAfee Endpoint Security, delivering enhanced protection and modern security features. It also includes configuring the Policy Orchestrator (ePO) to provide centralized management, streamlined policy enforcement, and improved visibility across all endpoints. The upgrade ensures stronger defense against threats, simplified administration, and consistent security compliance throughout the organization.', '2025-11-20 05:48:01.235792', '2025-11-24 06:20:05.477573', '108');
INSERT INTO projects VALUES (4, 'Patching', 'Responsible for ensuring timely and secure patching of all supported versions of Microsoft Windows and Red Hat Linux operating systems. This includes identifying applicable updates, deploying patches across environments, and maintaining compliance with organizational and security standards.', '2025-11-20 05:56:53.703789', '2025-11-20 05:56:53.703803', 'PS');
