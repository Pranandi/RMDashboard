import os, requests,datetime,sqlite3
from time import sleep
from customername import CustomerNameMapping as cn
#Read the file(.env) and set the environment variables
def load_env_file(file_path):
    with open(file_path) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value
load_env_file('.env')
main_url = os.environ.get('HIPPO_URL') # Get the Hippo URL from environment variable
token = os.environ.get('token') # Get the token from environment variable
#Get certificate using CN=hippo.it.savvis.net
cert_path = os.path.join('hippo.it.savvis.net.crt')
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json",
}
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
change_id_list = "0"
with open('no_tasks.txt') as f:
    no_tasks_change_ids = ','.join(set(f.read().splitlines()))
if no_tasks_change_ids:
    change_id_list = change_id_list + ',' + no_tasks_change_ids
#print(change_id_list)
cursor.execute(f"select change_number,change_id,final_status from change_details where change_status='CLOSED' and remedy_status!='Cancelled' and remedy_status!='Request Withdrawn' and change_id not in ({change_id_list}) and change_id not in (select distinct change_number_id from task_information) order by change_id asc")
results = cursor.fetchall()
processed_count = 0
for result in results: # Limiting to 10 records for testing, you can remove this condition to process all records
    ChangeId = result[0]
    change_id = result[1]
    change_status = result[2]
    cursor.execute("SELECT change_number_id from task_information where change_number_id = ?", (change_id,))
    if cursor.fetchone() is not None:
        print(f"Tasks for ChangeId {ChangeId} already exist in the database. Skipping API call.")
        continue
    print(f"{datetime.datetime.now()} - Processing ChangeId: {ChangeId}")
    url = f"{main_url}/api/activities/{ChangeId}/tasks/"
    arguments = { }
    try:
        print(f"{datetime.datetime.now()} - Making API call to: {url}")
        response = requests.get(url, headers=headers, verify=cert_path, params=arguments)
        if response.status_code == 200:
            #print("Request successful.")
            #Json Response converted to Python Dictionary
            tasks = response.json()
            if len(tasks) == 0:
                if str(change_id) not in no_tasks_change_ids.split(','):
                    with open('no_tasks.txt', 'a') as f:
                        f.write(f"{change_id}\n")
                print("--------------------------------------------------") 
                continue
            
            print(f"Total tasks retrieved for ChangeId {ChangeId}: {len(tasks)}")
            success_inserted_tasks = 0
            failed_inserted_tasks = 0
            failed_tasks = []
            for t in tasks:
                try:
                    manual_status = 'Unknown'
                    stage = t.get("stage","Unknown")
                    status = t.get("status","Unknown")
                    company_name = t.get("remedyCompanyName","Unknown")
                    if company_name:
                        company_name = cn().get_customer_name(company_name)
                    if stage == '(finished)' and status in ['Success','Warning']:
                        manual_status = status
                    elif change_status == 'Success':
                        manual_status = 'Success'
                    else:
                        manual_status = 'Unknown'
                    cursor.execute("INSERT INTO task_information (change_number_id, company_name, server_name, stage, status, started_date, updated_date, environment, environment_type, os,manual_status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (change_id, company_name, t.get("id"), t.get("stage","Unknown"), t.get("status",'Unknown'), t.get("started"), t.get("updated"), t.get("environment",'Unknown'), t.get("environmentType",'Unknown'), t.get("os",'Unknown'), manual_status))
                    conn.commit()
                    success_inserted_tasks += 1
                except Exception as e:
                    print(f"Failed to insert task for ChangeId {ChangeId}: {e}")
                    failed_inserted_tasks += 1
                    failed_tasks.append(t)
            if failed_inserted_tasks > 0:
                    print(f"Failed to insert {failed_inserted_tasks} tasks for ChangeId {ChangeId}. Failed tasks: {failed_tasks}")
                    #write it to text file
                    with open('failed_tasks.txt', 'a') as f:
                        f.write(f"Failed to insert {failed_inserted_tasks} tasks for ChangeId {ChangeId}. Failed tasks: {failed_tasks}\n")                
            print(f"Tasks for ChangeId {ChangeId} saved successfully. Total tasks: {len(tasks)}, Successfully inserted: {success_inserted_tasks}, Failed to insert: {failed_inserted_tasks}")
            print("--------------------------------------------------")                
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
        processed_count += 1
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    sleep(0.5)  # Sleep for 0.5 seconds between API calls to avoid overwhelming the server
    if processed_count%50 == 0: # Limiting to 10 records for testing, you can remove this condition to process all records
        print("Pausing for 5 seconds to avoid overwhelming the API...")
        sleep(5)  # Pause for 5 seconds before processing the next batch
        #break
conn.close()