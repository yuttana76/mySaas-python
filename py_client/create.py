import requests

headers = {'Authorization': 'Bearer 0fcf8c1fe99bcaebf77f94151d6dd47e1220b089'}
endpoint = "http://127.0.0.1:8000/api/products/" #http://127.0.0.1:8000/ 

data = {
    'title': 'Mr. Token'
    }

get_response = requests.post(endpoint,json=data,headers=headers) # json=data

print(get_response.json()) # print raw text response
