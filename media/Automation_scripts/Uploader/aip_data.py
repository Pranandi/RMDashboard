import os, requests,datetime,sqlite3,time

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute("delete from aip_data")
conn.commit()
cursor.execute("drop table if exists aip_data")
conn.commit()
cursor.execute("CREATE TABLE aip_data (id integer NOT NULL PRIMARY KEY AUTOINCREMENT, server varchar(255) NULL, inst_comp_name varchar(255) NULL, primary_ip varchar(50) NULL, inst_comp_status varchar(100) NULL, aip_status varchar(100) NULL, vpdc_profile varchar(255) NULL, customer_site_id varchar(100) NULL, customer_site_name varchar(255) NULL, rank varchar(50) NULL, physical_site_id varchar(100) NULL, support_region varchar(100) NULL, sales_product_line varchar(255) NULL, service_package varchar(255) NULL, created_at datetime NOT NULL, updated_at datetime NOT NULL);")
#read Excel file and insert into database one by one
import pandas as pd
df = pd.read_excel('media/Automation_scripts/Uploader/aip_data.xlsx')
for index, row in df.iterrows():
    data = []
    for column in df.columns:
        data.append(str(row[column]).strip())
    data.append(datetime.datetime.now())
    data.append(datetime.datetime.now())
    cursor.execute("insert into aip_data(server, inst_comp_name, primary_ip, inst_comp_status, aip_status, vpdc_profile, customer_site_id, customer_site_name, rank, physical_site_id, support_region, sales_product_line, service_package,created_at,updated_at) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data)
    print(f"Inserted row {index+1}")
    conn.commit()
    if index%50==0:
        print("Committed to database. Sleeping for 5 seconds...(?)",datetime.datetime.now())
        time.sleep(1)
conn.commit()