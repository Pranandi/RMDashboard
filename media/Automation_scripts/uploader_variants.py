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
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

cursor.execute("select project_id from uploader_projects")
for row in cursor.fetchall():
    variant_url = f"{main_url}/api/projects/{row[0]}"
    arguments = {}
    try:
        response = requests.get(variant_url, headers=headers, verify=cert_path, params=arguments)
        if response.status_code == 200:
            print("Request successful.")
            data = response.json()
            i=1;
            variants = data.get('variants', [])
            template_id = data.get('_id', '')
            project = data.get('id', '') + "-"+ data.get('title', '')
            team_id = data.get('_team', '')
            team_name = ""
            team_description = ""
            if team_id == "58d908c5650a8e14000a9ed0":
                team_name = "Global Release Management"
                team_description = "Responsible for OS Patching Software upgrades to core agents (virus protection, backup agents, monitoring agents)"
            for item in variants:
                created =item.get('createdAt', '')
                last_updated = item.get('updatedAt', '')
                variant_name = item.get('name', '')
                variant_description = item.get('description', '')
                default_variant = item.get('default', False)
                active = item.get('active', False)
                impacting = item.get('impacting', False)
                mop = item.get('mop', '')
                variant = project + " - " + variant_name
                default_project_variant = project if default_variant else ""
                
                cursor.execute("select * from uploader_variants where project = ? and variant_name = ?", (project, variant_name))
                existing_project = cursor.fetchone()
                if existing_project:
                    print(f"Project with project_id {project} & variant_name {variant_name} already exists. Skipping insertion.")
                else:
                    cursor.execute("insert into uploader_variants(template_id, last_updated, created, project,variant_name, variant_description, default_variant,active, impacting, mop, team_name,variant, default_project_variant, created_at, updated_at) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (template_id, last_updated, created, project,variant_name, variant_description, default_variant,active, impacting, mop, team_name,variant, default_project_variant, datetime.datetime.now(), datetime.datetime.now()))
                    conn.commit()
        else:
            print(f"Request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
conn.close()