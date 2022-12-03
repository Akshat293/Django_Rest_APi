import requests

endpoint='http://127.0.0.1:8000/api/products/'
data={
    'title':'All is well 1 2 3'
}
get_response=requests.post(endpoint,json=data)
print(get_response.status_code)
print(get_response.json())


# required field are required when validating with serelizable 

