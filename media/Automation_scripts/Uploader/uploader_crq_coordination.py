import sqlite3

conn = sqlite3.connect('uploader.sqlite3')
cursor = conn.cursor()
cursor.execute("create table if not exists  uploader_crq_coordination(id integer primary key autoincrement, coordination text, coordinator_company text, coordinator_organization text, workgroup text, change_coordinator text, task_name_1 text, task_summary_1 text)")
conn.commit()
cursor.execute("INSERT INTO uploader_crq_coordination(coordination, coordinator_company, coordinator_organization, workgroup, change_coordinator, task_name_1, task_summary_1) VALUES ('RM', 'Savvis', 'Operations', 'ReleaseMgmt', 'Satheesh Lal', 'RM Task', 'Carry out steps in MOP')")
cursor.execute("INSERT INTO uploader_crq_coordination(coordination, coordinator_company, coordinator_organization, workgroup, change_coordinator, task_name_1, task_summary_1) VALUES ('RM ZT', 'Savvis', 'Operations', 'ReleaseMgmt', 'Hippo Automation', '', '')")
cursor.execute("INSERT INTO uploader_crq_coordination(coordination, coordinator_company, coordinator_organization, workgroup, change_coordinator, task_name_1, task_summary_1) VALUES ('UNIX', 'Savvis', 'Operations', 'UNIX_T3', 'Default Operations', 'Unix Task', 'Carry out steps in MOP')")
cursor.execute("INSERT INTO uploader_crq_coordination(coordination, coordinator_company, coordinator_organization, workgroup, change_coordinator, task_name_1, task_summary_1) VALUES ('Windows', 'Savvis', 'Operations', 'Win_T3', 'Default Operations', 'Windows Task', 'Carry out steps in MOP')")
conn.commit()