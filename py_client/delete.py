import requests
productid=input("Enter the primary key")
try:
    productid=int(productid)
except:
    print(f"{productid} is not a valid id" )


if productid:
     endpoint=f'http://127.0.0.1:8000/api/products/{productid}/delete/'
     get_response=requests.delete(endpoint)
     print(get_response.status_code,get_response.status_code==204)
   


# required field are required when validating with serelizable 

