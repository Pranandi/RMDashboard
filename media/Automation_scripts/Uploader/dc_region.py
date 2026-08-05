import os, requests,datetime,sqlite3,time

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute("delete from dc_region")
conn.commit()
#read Excel file and insert into database one by one
import pandas as pd
df = pd.read_excel('media/Automation_scripts/Uploader/dc_region.xlsx')
for index, row in df.iterrows():
    data = []
    for column in df.columns:
        data.append(str(row[column]).strip())
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    cursor.execute("insert into dc_region(site_id, region, sub_region, country, city, scheduler_time_zone, created_at, updated_at) values(?,?,?,?,?,?,?,?)", data)
    print(f"Inserted row {index+1}")
    conn.commit()
    if index%50==0:
        print("Committed to database. Sleeping for 1 seconds...(?)",datetime.datetime.now())
        time.sleep(1)
conn.commit()