import sqlite3
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
from customername import CustomerNameMapping as cn
company_name_mapping = cn().get_all_mapped_names()

for new_name, old_names in company_name_mapping.items():
    for old_name in old_names:
        cursor.execute("update change_details set company_name = ? where company_name = ?", (new_name, old_name))
        cursor.execute("update task_information set company_name = ? where company_name = ?", (new_name, old_name))
        conn.commit()
'''
cursor.execute("select distinct company_name from change_details order by company_name")
companies = cursor.fetchall()
print("No of unique companies in change_details table: ", len(companies))
for company in companies:
    print(company[0])
cursor.execute("select distinct company_name from task_information order by company_name")
companies = cursor.fetchall()
print("No of unique companies in task_information table: ", len(companies))
for company in companies:
    print(company[0])'''
conn.close()