import sqlite3

conn = sqlite3.connect('uploader.sqlite3')
cursor = conn.cursor()
cursor.execute("create table if not exists  uploader_crq_client_approval(id integer primary key autoincrement, client text, template text, approval_note text)")
conn.commit()
cursor.execute("INSERT INTO uploader_crq_client_approval(client, template, approval_note) VALUES ('Savvis__Itential', 'PS - Scripted Patching', 'RM: Standard Monthly OS Patching as agreed with Nick Havard')")
cursor.execute("INSERT INTO uploader_crq_client_approval(client, template, approval_note) VALUES ('Savvis__HPNA', 'PS - Scripted Patching', 'RM: Standard Monthly OS Patching as agreed with Sidhanti Sudheendra')")
cursor.execute("INSERT INTO uploader_crq_client_approval(client, template, approval_note) VALUES ('Savvis__HPSA', 'PS - Scripted Patching', 'RM: Standard Monthly OS Patching as agreed with Gurdyal Singh')")
cursor.execute("INSERT INTO uploader_crq_client_approval(client, template, approval_note) VALUES ('Savvis__ActiveMQ', 'PS - Scripted Patching', 'RM: Standard Monthly OS Patching as agreed with David Stamper')")
cursor.execute("INSERT INTO uploader_crq_client_approval(client, template, approval_note) VALUES ('Savvis__HIE-Platform_PCI', 'PS - Scripted Patching', 'RM: Standard Monthly OS Patching as agreed with HIE Platform Team')")
cursor.execute("INSERT INTO uploader_crq_client_approval(client, template, approval_note) VALUES ('Savvis__OO', 'PS - Scripted Patching', 'RM: Standard Monthly OS Patching as agreed with Seethalakshmi Balachandran')")
conn.commit()