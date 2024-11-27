from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for products
products = []

@app.route('/products', methods=['POST'])
def create_product():

    data = request.json

    # Validate input
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400
    if not data.get("name"):
        return jsonify({"error": "Field 'name' is required"}), 400
    if not data.get("description"):
        return jsonify({"error": "Field 'description' is required"}), 400
    if not isinstance(data.get("price"), (int, float)):
        return jsonify({"error": "Field 'price' must be a number"}), 400

    # Create the product
    new_product = {
        "id": len(products) + 1,  # auto-increment ID
        "name": data["name"],
        "description": data["description"],
        "price": data["price"],
    }
    products.append(new_product)
    return jsonify(new_product), 201  # 201 Created

@app.route('/products', methods=['GET'])
def get_products():
#Retrieve list of products
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(debug=True)


