import requests
from getpass import getpass

endpoint = 'http://127.0.0.1:8000/api/auth/'
password = getpass()
auth_response = requests.post(
    endpoint, json={'username': 'cfe', 'password': password})

print(auth_response.json())

endpoint = 'http://127.0.0.1:8000/api/products/'
token = auth_response.json()['token']
headers = {
    'Authorization': f'Bearer {token}'
}
if auth_response.status_code == 200:
    get_response = requests.get(endpoint, headers=headers)

    data = get_response.json()
    result = data['results']
    next = data['next']
    if next is not None:
        get_response = requests.get(next, headers=headers)
        data = get_response.json()
        result += data['results']

        print(result)

