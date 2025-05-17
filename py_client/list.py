import requests
from getpass import getpass


auth_endpoint = "http://127.0.0.1:8000/api/auth/"
user=input("Username: ")
password = getpass("Password: ")
auth_response = requests.post(auth_endpoint,json={"username":user,"password":password   })
print(auth_response.json()) # print raw text response

if auth_response.status_code == 200:
    token = auth_response.json().get("token")
    headers = {
        "Authorization": f"Token {token}"
        # "Authorization": f"Bearer {token}"
    }

    endpoint = "http://127.0.0.1:8000/api/products/"
    get_response = requests.get(endpoint,headers=headers)
    print(get_response.json()) # print raw text response

    # data = get_response.json()
    # next_url = data.get("next")
    # if next_url is not None:
    #     endpoint = next_url
    #     get_response = requests.get(endpoint,headers=headers)
    #     print(get_response.json())

