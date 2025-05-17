import requests

product_id = input("Enter product ID: ")

try:
    product_id = int(product_id)
except ValueError:
    product_id = None
    print("Invalid product ID. Please enter a valid integer.")

if product_id:
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/" 

    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code == 204)
