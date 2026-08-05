-- Table: uploader_projects
-- Mode: IN-PLACE
-- Backup Date: 2026-05-13 10:44:07
-- Row Count: 48
-- Hash: 2f36062295b922a2b7dd70100cd974ea

DROP TABLE IF EXISTS uploader_projects;
CREATE TABLE "uploader_projects" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "template_id" varchar(100) NOT NULL, "project_id" varchar(100) NOT NULL, "project_title" varchar(255) NOT NULL, "project" varchar(255) NOT NULL, "change_title" varchar(255) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);

INSERT INTO uploader_projects VALUES (1, '64d0be7a9fc1120011949ac1', '109', 'HIERM-109-Opsware Agent Upgrade', '109 - HIERM-109-Opsware Agent Upgrade', 'HIERM-109A-', '2026-05-12 13:13:39.680684', '2026-05-12 13:13:39.680689');
INSERT INTO uploader_projects VALUES (2, '64493b0ade57390011d6d103', '201', 'Bruce Test Project', '201 - Bruce Test Project', 'HIERM-201A-', '2026-05-12 13:13:39.706122', '2026-05-12 13:13:39.706128');
INSERT INTO uploader_projects VALUES (3, '6278a4771c0cbd0011136427', '108', 'HIERM-108-Mcafee ENS Upgrade', '108 - HIERM-108-Mcafee ENS Upgrade', 'HIERM-108A-', '2026-05-12 13:13:39.722555', '2026-05-12 13:13:39.722560');
INSERT INTO uploader_projects VALUES (4, '60dde98212daae00113e2454', '107', 'Windows Spooler Service Disable', '107 - Windows Spooler Service Disable', 'HIERM-107A-', '2026-05-12 13:13:39.738765', '2026-05-12 13:13:39.738770');
INSERT INTO uploader_projects VALUES (5, '604607b54485050011e921ff', '106', 'Static Route Changes', '106 - Static Route Changes', 'HIERM-106A-', '2026-05-12 13:13:39.759797', '2026-05-12 13:13:39.759803');
INSERT INTO uploader_projects VALUES (6, '602534ed901e8100118b3992', '105', 'CVE-2021-24074 Windows Source Routing', '105 - CVE-2021-24074 Windows Source Routing', 'HIERM-105A-', '2026-05-12 13:13:39.779222', '2026-05-12 13:13:39.779227');
INSERT INTO uploader_projects VALUES (7, '5fda28a328c9250011ad4fae', '104', 'HP Proliant Firmware Updates', '104 - HP Proliant Firmware Updates', 'HIERM-104A-', '2026-05-12 13:13:39.795952', '2026-05-12 13:13:39.795957');
INSERT INTO uploader_projects VALUES (8, '5fbfba1a28c9250011ab5eb5', '103', 'Flexera', '103 - Flexera', 'HIERM-103A-', '2026-05-12 13:13:39.812772', '2026-05-12 13:13:39.812777');
INSERT INTO uploader_projects VALUES (9, '5f1f8eea491cf300112a58c1', '97', 'McAfee Endpoint Security Protection', '97 - McAfee Endpoint Security Protection', 'HIERM-97A-', '2026-05-12 13:13:39.829460', '2026-05-12 13:13:39.829465');
INSERT INTO uploader_projects VALUES (10, '5eda5a3b381cb30011cdf1dd', '83', 'WSUS Migration', '83 - WSUS Migration', 'HIERM-83A-', '2026-05-12 13:13:39.845436', '2026-05-12 13:13:39.845441');
INSERT INTO uploader_projects VALUES (11, '5e39409ec4b467001160b318', '100', 'RHSM Migration', '100 - RHSM Migration', 'HIERM-100A-', '2026-05-12 13:13:39.861527', '2026-05-12 13:13:39.861532');
INSERT INTO uploader_projects VALUES (12, '5dbfe2be108931000f56245f', '98', 'Managed VM Automation', '98 - Managed VM Automation', 'HIERM-98A-', '2026-05-12 13:13:39.877677', '2026-05-12 13:13:39.877682');
INSERT INTO uploader_projects VALUES (13, '5d36c50628e480000f57c23a', '96', 'Cisco ASA Upgrade', '96 - Cisco ASA Upgrade', 'HIERM-96A-', '2026-05-12 13:13:39.892903', '2026-05-12 13:13:39.892908');
INSERT INTO uploader_projects VALUES (14, '5cecf775a34faa2ee3a6f3ae', '101', 'GOC Change Template', '101 - GOC Change Template', 'HIERM-101A-', '2026-05-12 13:13:39.907133', '2026-05-12 13:13:39.907136');
INSERT INTO uploader_projects VALUES (15, '5c862b7f29fcd2000f1d9fee', '501', 'Zero Touch Server Decommissioning', '501 - Zero Touch Server Decommissioning', 'HIERM-501A-', '2026-05-12 13:13:39.920667', '2026-05-12 13:13:39.920671');
INSERT INTO uploader_projects VALUES (16, '5c4b15c41f8259000e0788a2', 'PM', 'Patch Management', 'PM - Patch Management', 'HIERM-PMA-', '2026-05-12 13:13:39.935668', '2026-05-12 13:13:39.935673');
INSERT INTO uploader_projects VALUES (17, '5bfd1e4dcbf82c000ee31ab2', '92', 'HPSA Agent Cleanup', '92 - HPSA Agent Cleanup', 'HIERM-92A-', '2026-05-12 13:13:39.949366', '2026-05-12 13:13:39.949371');
INSERT INTO uploader_projects VALUES (18, '5bfd1e19cbf82c000ee31ab1', '45', 'Windows Service Pack', '45 - Windows Service Pack', 'HIERM-45A-', '2026-05-12 13:13:39.965399', '2026-05-12 13:13:39.965404');
INSERT INTO uploader_projects VALUES (19, '5be20c66625a67000e6b280b', '95', 'Cisco ASA Remote Code Execution', '95 - Cisco ASA Remote Code Execution', 'HIERM-95A-', '2026-05-12 13:13:39.980475', '2026-05-12 13:13:39.980480');
INSERT INTO uploader_projects VALUES (20, '5be0196b625a67000e6b02c6', '93', 'Cisco ASA Security Advisory Cisco-Sa-20180418', '93 - Cisco ASA Security Advisory Cisco-Sa-20180418', 'HIERM-93A-', '2026-05-12 13:13:39.995573', '2026-05-12 13:13:39.995578');
INSERT INTO uploader_projects VALUES (21, '5ba8b30acf7bbb000e8732c9', 'RA', 'Reboot Only', 'RA - Reboot Only', 'HIERM-RAA-', '2026-05-12 13:13:40.011444', '2026-05-12 13:13:40.011449');
INSERT INTO uploader_projects VALUES (22, '5a9022ff307f050014003bb9', '999', 'HIERM-999A - Automation Test Project', '999 - HIERM-999A - Automation Test Project', 'HIERM-999A-', '2026-05-12 13:13:40.028918', '2026-05-12 13:13:40.028923');
INSERT INTO uploader_projects VALUES (23, '5a8d4ed1307f050014003905', 'PH', 'Legacy HPSA Patching', 'PH - Legacy HPSA Patching', 'HIERM-PHA-', '2026-05-12 13:13:40.045619', '2026-05-12 13:13:40.045624');
INSERT INTO uploader_projects VALUES (24, '5a8553132baa6d0014dbd048', 'PS', 'Scripted Patching', 'PS - Scripted Patching', 'HIERM-PSA-', '2026-05-12 13:13:40.062385', '2026-05-12 13:13:40.062391');
INSERT INTO uploader_projects VALUES (25, '5a4f57b1e72ad9002609cda5', '90', 'HIERM-90-Meltdown and Spectre - CVE-2017-5715, CVE-2017-5753, CVE-2017-5754', '90 - HIERM-90-Meltdown and Spectre - CVE-2017-5715, CVE-2017-5753, CVE-2017-5754', 'HIERM-90A-', '2026-05-12 13:13:40.081971', '2026-05-12 13:13:40.081977');
INSERT INTO uploader_projects VALUES (26, '5a27bfb138cf580014efcfe8', '85', 'Security Appliance Upgrade', '85 - Security Appliance Upgrade', 'HIERM-85A-', '2026-05-12 13:13:40.098140', '2026-05-12 13:13:40.098145');
INSERT INTO uploader_projects VALUES (27, '5a27bf5d38cf580014efcfe7', '80', 'Cisco ASA Upgrade', '80 - Cisco ASA Upgrade', 'HIERM-80A-', '2026-05-12 13:13:40.114070', '2026-05-12 13:13:40.114076');
INSERT INTO uploader_projects VALUES (28, '5a27be2e38cf580014efcfdc', '82', 'Silverlight', '82 - Silverlight', 'HIERM-82A-', '2026-05-12 13:13:40.130199', '2026-05-12 13:13:40.130205');
INSERT INTO uploader_projects VALUES (29, '5a27bd6a38cf580014efcfbc', '79', 'HBA Storage Stability', '79 - HBA Storage Stability', 'HIERM-79A-', '2026-05-12 13:13:40.146382', '2026-05-12 13:13:40.146387');
INSERT INTO uploader_projects VALUES (30, '5a27bcdc38cf580014efcf8c', '59', 'SIA Upgrade', '59 - SIA Upgrade', 'HIERM-59A-', '2026-05-12 13:13:40.162261', '2026-05-12 13:13:40.162266');
INSERT INTO uploader_projects VALUES (31, '5a27bc5f38cf580014efcf89', '58', 'Powershell V2 Upgrade', '58 - Powershell V2 Upgrade', 'HIERM-58A-', '2026-05-12 13:13:40.178730', '2026-05-12 13:13:40.178735');
INSERT INTO uploader_projects VALUES (32, '5829a4b82f2cca633e209f38', '81', 'McAfee_Agent_Handlers', '81 - McAfee_Agent_Handlers', 'HIERM-81A-', '2026-05-12 13:13:40.195969', '2026-05-12 13:13:40.195975');
INSERT INTO uploader_projects VALUES (33, '5760202828a68f28168e0e1c', '74', 'Internet Explorer Upgrade', '74 - Internet Explorer Upgrade', 'HIERM-74A-', '2026-05-12 13:13:40.213081', '2026-05-12 13:13:40.213086');
INSERT INTO uploader_projects VALUES (34, '57601fa728a68f28168e0e1b', '76', 'VMTools Upgrade', '76 - VMTools Upgrade', 'HIERM-76A-', '2026-05-12 13:13:40.230171', '2026-05-12 13:13:40.230177');
INSERT INTO uploader_projects VALUES (35, '56600ba7c9ff8f57347f17f4', '32', 'Disable HP SMH', '32 - Disable HP SMH', 'HIERM-32A-', '2026-05-12 13:13:40.246601', '2026-05-12 13:13:40.246606');
INSERT INTO uploader_projects VALUES (36, '5643502a403a4ac20e3fadea', '99', 'Adhoc Patching Requests', '99 - Adhoc Patching Requests', 'HIERM-99A-', '2026-05-12 13:13:40.262319', '2026-05-12 13:13:40.262324');
INSERT INTO uploader_projects VALUES (37, '56433fde403a4ac20e3f9c40', '73', 'McAfee Agent Upgrade', '73 - McAfee Agent Upgrade', 'HIERM-73A-', '2026-05-12 13:13:40.279201', '2026-05-12 13:13:40.279206');
INSERT INTO uploader_projects VALUES (38, '56433fc0403a4ac20e3f9c3c', '72', 'McAfee VirusScan 8.8 Upgrade', '72 - McAfee VirusScan 8.8 Upgrade', 'HIERM-72A-', '2026-05-12 13:13:40.295783', '2026-05-12 13:13:40.295789');
INSERT INTO uploader_projects VALUES (39, '56433f8d403a4ac20e3f9c3b', '71', 'McAfee VirusScan Agent + Engine Upgrade', '71 - McAfee VirusScan Agent + Engine Upgrade', 'HIERM-71A-', '2026-05-12 13:13:40.312132', '2026-05-12 13:13:40.312137');
INSERT INTO uploader_projects VALUES (40, '56433f58403a4ac20e3f9c2d', '70', 'CLC McAfee Agent Install/Upgrade', '70 - CLC McAfee Agent Install/Upgrade', 'HIERM-70A-', '2026-05-12 13:13:40.329079', '2026-05-12 13:13:40.329084');
INSERT INTO uploader_projects VALUES (41, '56433e75403a4ac20e3f9c1a', '69', 'McAfee AntiVirus Migration - Allen & Overy Variant', '69 - McAfee AntiVirus Migration - Allen & Overy Variant', 'HIERM-69A-', '2026-05-12 13:13:40.343662', '2026-05-12 13:13:40.343667');
INSERT INTO uploader_projects VALUES (42, '55e49759eef828d17a1a7332', '61', 'HIERM-61A_CLC_VM_McAfee', '61 - HIERM-61A_CLC_VM_McAfee', 'HIERM-61A-', '2026-05-12 13:13:40.358243', '2026-05-12 13:13:40.358248');
INSERT INTO uploader_projects VALUES (43, '55a4e26a750cdbc067a4506b', '55', 'NetBackup Upgrades', '55 - NetBackup Upgrades', 'HIERM-55A-', '2026-05-12 13:13:40.372188', '2026-05-12 13:13:40.372194');
INSERT INTO uploader_projects VALUES (44, '55318b1054deecb71f5b5e0c', '49', 'HPSA Agent Upgrades', '49 - HPSA Agent Upgrades', 'HIERM-49A-', '2026-05-12 13:13:40.387370', '2026-05-12 13:13:40.387375');
INSERT INTO uploader_projects VALUES (45, '55318aed54deecb71f5b5e08', '63', 'McAfee AntiVirus 5700 Engine', '63 - McAfee AntiVirus 5700 Engine', 'HIERM-63A-', '2026-05-12 13:13:40.403003', '2026-05-12 13:13:40.403009');
INSERT INTO uploader_projects VALUES (46, '552fe95058698e9863fe5659', '47', 'Sysinternals Tools Update', '47 - Sysinternals Tools Update', 'HIERM-47A-', '2026-05-12 13:13:40.418118', '2026-05-12 13:13:40.418122');
INSERT INTO uploader_projects VALUES (47, '552fe92c58698e9863fe5658', '00', 'Adhoc Patching', '00 - Adhoc Patching', 'HIERM-00A-', '2026-05-12 13:13:40.432316', '2026-05-12 13:13:40.432321');
INSERT INTO uploader_projects VALUES (48, '552fe90158698e9863fe5657', '23', 'McAfee AntiVirus Migration', '23 - McAfee AntiVirus Migration', 'HIERM-23A-', '2026-05-12 13:13:40.449153', '2026-05-12 13:13:40.449158');
