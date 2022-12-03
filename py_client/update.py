import requests

endpoint='http://127.0.0.1:8000/api/products/1/update/'
data={
    'title':'All is well I am here here',
    'price':123.01
}
get_response=requests.put(endpoint,json=data)
print(get_response.status_code)
print(get_response.json())


# required field are required when validating with serelizable 

