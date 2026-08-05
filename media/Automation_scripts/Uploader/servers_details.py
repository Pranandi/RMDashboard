import os, requests,datetime,sqlite3,time

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute("delete from server_details")
conn.commit()
#read Excel file and insert into database one by one
import pandas as pd
df = pd.read_excel('media/Automation_scripts/Uploader/servers.xlsx')
for index, row in df.iterrows():
    data = ['Savvis']
    #print(df.columns)
    for column in df.columns:
        value = str(row[column]).strip() if pd.notna(row[column]) else None
        data.append(value)
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    cursor.execute("insert into server_details(client,batch, server, operating_system, application, environment, server_type, notes, include, created_at, updated_at) values(?,?,?,?,?,?,?,?,?,?,?)", data)
    print(f"Inserted row {index+1}")
    conn.commit()
    if index%50==0:
        print("Committed to database. Sleeping for 1 seconds...(?)",datetime.datetime.now())
        time.sleep(1)
conn.commit()