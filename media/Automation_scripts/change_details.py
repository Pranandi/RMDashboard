import os, requests,datetime,sqlite3,random
from customername import CustomerNameMapping as cn
def load_env_file(file_path):
    with open(file_path) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

def get_remedy_data(change_id, remedy_url, headers, cert_path):
    url = f"{remedy_url}/{change_id}"
    try:
        response = requests.get(url, headers=headers, verify=cert_path)
        if response.status_code == 200:
            item = response.json()
            startdate = item.get('schedule', {}).get('scheduledDates', {}).get('startDate')
            enddate = item.get('schedule', {}).get('scheduledDates', {}).get('endDate')
            remedy_status = (item.get('statusInformation', {}).get('displayReasonName', '')).strip()
            if not remedy_status:
                remedy_status = (item.get('statusInformation', {}).get('reason', '')).strip()
            remedy_reason = (item.get('statusInformation', {}).get('reason', '')).strip()
            change_status = (item.get('statusInformation', {}).get('current', '')).strip()
            company_name = (item.get('location', {}).get('company', '')).strip()
            return {
                "startdate": startdate,
                "enddate": enddate,
                "remedy_status": remedy_status,
                "remedy_reason": remedy_reason,
                "change_status": change_status,
                "company_name": company_name
            }
        else:
            print(f"Failed to fetch remedy data for ChangeId {change_id}. Status code: {response.status_code}")
            return {}
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching remedy data for ChangeId {change_id}: {e}")
        return {}
load_env_file('.env')
main_url = os.environ.get('HIPPO_URL') # Get the Hippo URL from environment variable
token = os.environ.get('token') # Get the token from environment variable
#Get certificate using CN=hippo.it.savvis.net
cert_path = os.path.join('hippo.it.savvis.net.crt')
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json",
}
change_url = f"{main_url}/api/activities"
remedy_url = f"{main_url}/api/remedy/change"
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

start_date = (datetime.datetime.now() - datetime.timedelta(days=10)).date().isoformat()  # Fetch changes from the past 10 days
end_date = (datetime.datetime.now()).date().isoformat()  # Up to today's date
day_diff = random.choice(range(28, 35))  # Random day difference between 28 and 35 to avoid fetching data in fixed intervals which may cause performance issues or hitting API rate limits. This will help to distribute the load on the API and database more evenly over time.

#if monday, then fetch changes from the past 180 days to get more data for analysis and reporting, otherwise fetch changes from the past 10 days to keep the data updated. This is because on every monday we need to send report to management and they need more data for better analysis and decision making.
if datetime.datetime.now().weekday() == 0:  # Monday
    start_date = (datetime.datetime.now() - datetime.timedelta(days=180)).date().isoformat()  # Fetch changes from the past 180 days
    
#fetch the current date
while start_date < end_date:  
    temp_end_date = (datetime.datetime.strptime(start_date, "%Y-%m-%d") + datetime.timedelta(days=day_diff)).date().isoformat()  
    if temp_end_date > end_date:
        temp_end_date = end_date
    arguments = {
        "started": start_date,
        "ended": temp_end_date
    }
    print(f"Fetching changes from {start_date} to {temp_end_date}...")
    try:
        response = requests.get(change_url, headers=headers, verify=cert_path, params=arguments)
        if response.status_code == 200:
            print("Request successful.")
            #Json Response converted to Python Dictionary
            data = response.json()       
            already_exists_count = 0
            inserted_count = 0
            status_updated = 0
            non_valid_records = 0
            for item in data:
                project_type = item.get('projectType', '').strip()
                subtype = item.get('subType', '').strip()
                title = item.get('title', '').strip()
                type = item.get('type', '').strip()
                status = item.get('status', '').strip()
                change_number = item.get('id')
                if title.startswith('HIERM-') and project_type not in ['501','101']:
                    if cursor.execute("SELECT * FROM change_details WHERE change_number = ?", (change_number,)).fetchone() is None :
                        remedy = get_remedy_data(change_number, remedy_url, headers, cert_path)                            
                        if remedy and remedy.get('change_status') == 'CLOSED' and remedy.get('remedy_status') not in ['Cancelled', 'Request Withdrawn']:
                            remedy_status = remedy.get('remedy_status')
                            company_name = remedy.get('company_name')
                            remedy_reason = remedy.get('remedy_reason')
                            change_status = remedy.get('change_status')
                            if company_name:
                                company_name = cn().get_customer_name(company_name)
                            if project_type is None or project_type == '':
                                title_parts = title.split('-')
                                if title_parts[1].endswith('A'):
                                    project_type = title_parts[1][:-1]
                                else:
                                    project_type = title_parts[1]
                            final_status = 'Unknown'
                            if remedy_status == 'Successful':
                                final_status = 'Success'
                            elif remedy_status.startswith('Unsuccessful'):
                                final_status = 'Failed'
                            elif remedy_status == 'Partial Complete':
                                final_status = 'Partial'
                            print(f"Inserting Change {change_number} for company '{company_name}' with project type '{project_type}' and title '{title}' into the database.")
                            cursor.execute("INSERT INTO change_details (change_number, title, type, status, project_type, sub_type, zerotouch, startdate, enddate, remedy_status, remedy_reason, change_status, company_name,final_status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (change_number, title, type, status, project_type, subtype, item.get('isFullAutomation', False), remedy.get('startdate'), remedy.get('enddate'), remedy_status, remedy_reason, change_status, company_name, final_status))
                            conn.commit()
                            inserted_count += 1
                        else:
                            print(f"Skipping ChangeId {change_number} as it is not closed or failed to fetch remedy data.")
                    else:
                        #print(f"ChangeId {change_number} already exists in the database.")
                        already_exists_count += 1
                else:
                    non_valid_records += 1
            if inserted_count > 0:
                message = "Data inserted successfully."
                if inserted_count > 0:
                    message += f"{inserted_count} new records added."
                if already_exists_count > 0:
                    message += f"{already_exists_count} records already exist."
                if non_valid_records > 0:
                    message += f"{non_valid_records} records were not belongs release management."
            else:
                message = f"No new records were added. All records({already_exists_count + non_valid_records}) already exist or no valid records found."
            print(message)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(response.text)
        start_date = temp_end_date
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
conn.close()