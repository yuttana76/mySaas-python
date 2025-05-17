import requests

endpoint = "http://127.0.0.1:8000/api/products/9999/" #http://127.0.0.1:8000/ 

get_response = requests.get(endpoint)

print(get_response.json()) # print raw text response
