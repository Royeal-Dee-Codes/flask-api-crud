from flask import jsonify
from data import product_records


def product_create(request):
    post_data = request.form if request.form else request.get_json()
    product = {
        'product_id': int(len(product_records) + 1),
        'name': post_data['name'],
        'description': post_data['description'],
        'price': post_data['price'],
        'active': post_data.get('active', True)
    }
    product_records.append(product)
    return jsonify({"message": f"product {product['name']}  has been added.", "product": product}), 201


def product_get_by_id(product_id):
    print("product_records")
    for product in product_records:
        if product['product_id'] == int(product_id):
            return jsonify({"message": "product found", "results": product}), 200
    return jsonify({"message": f"product with product_id {product_id} not found."}), 404


def product_update_by_id(request, product_id):
    post_data = request.form if request.form else request.get_json()
    for product in product_records:
        if product['product_id'] == int(product_id):
            product['name'] = post_data.get('name', product['name'])
            product['description'] = post_data.get('description', product['description'])
            product['price'] = post_data.get('price', product['price'])
            product['active'] = post_data.get('active', product['active'])
            return jsonify({"message": f"product {product['name']} has been updated.", "product": product}), 200
    return jsonify({"message": f"product with product_id {product_id} not found."}), 404


def product_delete_by_id(product_id):
    for product in product_records:
        if product['product_id'] == int(product_id):
            product_records.remove(product)
            return jsonify({"message": f"product with product_id {product_id} has been deleted."}), 200
    return jsonify({"message": f"product with product_id {product_id} not found."}), 404


def get_all_products():
    return jsonify({"message": "products retrieved", "results": product_records}), 200


def get_active_products():
    active_products = [p for p in product_records if p['active']]
    return jsonify({"message": "active products retrieved", "results": active_products}), 200


def update_product_activity(request, product_id):
    post_data = request.form if request.form else request.get_json()
    active_status = post_data.get('active')

    if active_status is None:
        return jsonify({"massage": "active statis is required."}), 400

    for product in product_records:
        if product['product_id'] == int(product_id):
            product['active'] = active_status
            return jsonify({"message": f"product {product['name']} active status has been updated."}), 200
    return jsonify({"message": f"product with product_id {product_id} not found."}), 404
