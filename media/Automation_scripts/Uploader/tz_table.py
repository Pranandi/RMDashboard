import os, requests,datetime,sqlite3,time

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute("delete from timezone_table")
conn.commit()
#read Excel file and insert into database one by one
import pandas as pd
df = pd.read_excel('media/Automation_scripts/Uploader/tz_table.xlsx')
for index, row in df.iterrows():
    data = []
    #print(df.columns)
    for column in df.columns:
        data.append(str(row[column]).strip())
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    cursor.execute("insert into timezone_table(time_zone,remedy_tz_dst_inactive,remedy_tz_dst_active,non_dst_offset_hours, dst_offset, offset_mins, dst_start_time, dst_end_time, utc_offset, daylight_savings_start, daylight_savings_end, created_at, updated_at) values(?,?,?,?,?,?,?,?,?,?,?,?,?)", data)
    print(f"Inserted row {index+1}")
    conn.commit()
    if index%50==0:
        print("Committed to database. Sleeping for 1 seconds...(?)",datetime.datetime.now())
        time.sleep(1)
conn.commit()