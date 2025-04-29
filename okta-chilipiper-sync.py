import requests
import json
import secrets_file

cp_header = {
    "accept": "*/*",
    "Content-Type": "application/json",
    "Authorization": secrets_file.api_key,
}

okta_header = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": secrets_file.okta_api_key
}

# confirms (does not return) tenant_id (not needed every time)
"""def get_cp_tenant_id():
    tenant_url = secrets_file.ab_cp_url + "/v1/org/tenant/get/getweave"
    response = requests.get(tenant_url, headers=cp_header)"""

def get_all_chilipiper_users():
    parameters = {
        "pageSize": 100,
    }
    lists_users_url = secrets_file.ab_cp_url + "/users?"
    response = requests.get(lists_users_url, params=parameters, headers=cp_header)
    response_code = response.status_code
    data = json.dumps(response.text, indent=4)
    print("response code: " + str(response_code))
    print(data)

def find_cp_user(email):
    find_cp_url = secrets_file.ab_cp_url + "/v1/getweave/user/find"
    parameters = {
        "query": email,
        "page": 1,
        "pageSize": 50
    }
    response = requests.get(find_cp_url, headers=cp_header, params=parameters)
    data = json.dumps(response.text, indent=4)
    print(data)


def get_okta_chilipiper_users():
    # Chili Piper Okta App ID in secrets file
    all_assigned_users = []
    parameters = {

    }
    okta_url = secrets_file.ab_otka_url + "/api/v1/apps/" + secrets_file.chilipiper_appId + "/users"
    response = requests.get(okta_url, params=parameters, headers=okta_header)
    json_data = response.json()
    for item in json_data:
        all_assigned_users.append(item["credentials"]["userName"])
    return all_assigned_users


# all_cp_users = get_okta_chilipiper_users()
find_cp_user("kaeley.scruggs@getweave.com")