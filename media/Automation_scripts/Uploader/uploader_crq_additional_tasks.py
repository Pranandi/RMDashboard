import sqlite3

conn = sqlite3.connect('uploader.sqlite3')
cursor = conn.cursor()
cursor.execute("create table if not exists  uploader_crq_additional_tasks(id integer primary key autoincrement, task_name text, summary text, assignee text)")
conn.commit()
cursor.execute("INSERT INTO uploader_crq_additional_tasks(task_name, summary, assignee) VALUES ('RM Task', 'Carry out steps in MOP', 'ReleaseMgmt')")
cursor.execute("INSERT INTO uploader_crq_additional_tasks(task_name, summary, assignee) VALUES ('DB MSSQL Task', 'Carry out steps in MOP', 'Database_MSSQL')")
cursor.execute("INSERT INTO uploader_crq_additional_tasks(task_name, summary, assignee) VALUES ('DB Oracle Task', 'Carry out steps in MOP', 'Database_OracleMySQL')")
cursor.execute("INSERT INTO uploader_crq_additional_tasks(task_name, summary, assignee) VALUES ('Backup Task', 'Carry out steps in MOP', 'Backup')")
cursor.execute("INSERT INTO uploader_crq_additional_tasks(task_name, summary, assignee) VALUES ('ADAPTIVE Unix Middleware', 'Carry out steps in MOP', 'ADAPTIVE_Unix_Middleware')")
cursor.execute("INSERT INTO uploader_crq_additional_tasks(task_name, summary, assignee) VALUES ('IT Applications', 'Carry out steps in MOP', 'Applications')")
conn.commit()