import requests

endpoint = "http://127.0.0.1:8000/api/products/1/update/" #http://127.0.0.1:8000/ 

data = {
    "title": "Car Updated 1",
    "price": 123.45,
}

get_response = requests.put(endpoint, json=data)

print(get_response.json()) # print raw text response
