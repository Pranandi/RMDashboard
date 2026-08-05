import os, requests,datetime,sqlite3,random
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
project_url = f"{main_url}/api/projects"
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
arguments = {}
try:
    response = requests.get(project_url, headers=headers, verify=cert_path, params=arguments)
    if response.status_code == 200:
        print("Request successful.")
        data = response.json()
        i=1;
        for item in data:
            teams = item.get('teams', [])
            #if "global_release_management" in teams:
            ins_data = [item.get('_id', ''), item.get('id', ''), item.get('title', '')]
            ins_data.append(ins_data[1]+" - "+ins_data[2])
            ins_data.append("HIERM-"+ins_data[1]+"A-")
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ins_data.append(timestamp)
            ins_data.append(timestamp)
            cursor.execute("select * from uploader_projects where project_id = ?", (ins_data[1],))
            existing_project = cursor.fetchone()
            if existing_project:
                print(f"Project with project_id {ins_data[1]} already exists. Skipping insertion.")
            else:
                cursor.execute("insert into uploader_projects(template_id, project_id, project_title, project, change_title, created_at, updated_at) values (?, ?, ?, ?, ?, ?, ?)", ins_data)
                conn.commit()
    else:
        print(f"Request failed with status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred while making the request: {e}")
conn.close()