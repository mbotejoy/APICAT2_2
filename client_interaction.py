import http.client
import json

# Base URL for the API
BASE_URL = "127.0.0.1"
PORT = 5000
ENDPOINT = "/products"

def add_product(name, description, price):
    """
    Adds a new product by sending a POST request.
    :param name: Name of the product
    :param description: Description of the product
    :param price: Price of the product
    """
    product_data = {
        "name": name,
        "description": description,
        "price": price
    }

    # Create connection
    conn = http.client.HTTPConnection(BASE_URL, PORT)

    # Send POST request
    headers = {"Content-Type": "application/json"}
    conn.request("POST", ENDPOINT, body=json.dumps(product_data), headers=headers)

    # Get response
    response = conn.getresponse()
    if response.status == 201:
        print("Product added successfully:", json.loads(response.read().decode()))
    elif response.status == 400:
        print("Error:", json.loads(response.read().decode()))
    else:
        print("Unexpected response:", response.status, response.read().decode())

    # Close connection
    conn.close()

def get_all_products():
    """
    Retrieves and prints the list of all products.
    """
    # Create connection
    conn = http.client.HTTPConnection(BASE_URL, PORT)

    # Send GET request
    conn.request("GET", ENDPOINT)

    # Get response
    response = conn.getresponse()
    if response.status == 200:
        products = json.loads(response.read().decode())
        print("List of all products:")
        print(json.dumps(products, indent=4))  # Pretty-print the JSON
    else:
        print("Unexpected response:", response.status, response.read().decode())

    # Close connection
    conn.close()

if __name__ == "__main__":
    # Add a few products
    add_product("Laptop", "A high-performance laptop", 999.99)
    add_product("Smartphone", "Latest model smartphone", 699.99)
    add_product("Tablet", "Compact and lightweight tablet", 499.99)

    # Retrieve and print all products
    get_all_products()
