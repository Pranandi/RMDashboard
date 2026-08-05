token = "<|TOKEN_VALUE|>" # Replace <TOKEN_VALUE> with your actual token which you have to get from Hippo portal or Me

import requests,os
#Get certificate using CN=hippo.it.savvis.net
cert_path = os.path.join('hippo.it.savvis.net.crt')
MainUrl = "https://hippo.it.savvis.net:443"
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json",
}

#starts here
# Fetch Change details from DB through Hippo API and Filter by title (HIERM)
url = f"{MainUrl}/api/activities"
arguments = {
   "started": "2026-01-29",
    "ended": "2026-01-30",
    "type": "Execution"
}
'''
#Fetch Change Status Update & other informations from Remedy through Hippo API
ChangeId="CRQ000000604406"
url = f"{MainUrl}/api/remedy/change/{ChangeId}"
arguments = { }


#Fetch the Task Information from Hippo
ActivityId="CRQ000000604406"
url = f"{MainUrl}/api/activities/{ActivityId}/tasks/"
arguments = { }
'''
#Ends Here
try:
    response = requests.get(url, headers=headers, verify=cert_path, params=arguments)
    if response.status_code == 200:
        print("Request successful.")
        #Json Response converted to Python Dictionary
        data = response.json()
        print(data)

    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")