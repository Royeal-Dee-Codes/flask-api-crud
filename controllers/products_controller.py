from flask import jsonify
from data import product_records


def product_create(request):
    data = request.form if request.form else request.get_json()
    product = {
        'product_id': str(len(product_records) + 1),
        'product_name': data['product_name'],
        'description': data['description'],
        'price': data['price'],
        'active': data.get('active', True)
    }
    product_records.append(product)
    return jsonify({"message": f"Product {product['product_name']}  has been added."}), 201


def product_get_by_id(product_id):
    for product in product_records:
        if product['product_id'] == product_id:
            return jsonify({"message": "Product found", "results": product}), 200
        return jsonify({"message": f"Product with product_id {product_id} not found."}), 404


def product_update_by_id(request, product_id):
    data = request.form if request.form else request.get_json()
    for product in product_records:
        if product['product_id'] == product_id:
            product['product_name'] = data.get('product_name', product['product_name'])
            product['description'] = data.get('description', product['description'])
            product['price'] = data.get('price', product['price'])
            product['active'] = data.get('active', product['active'])
            product_records.append(product)
            return jsonify({"message": f"Product {product['product_name']} has been updated."}), 200
        return jsonify({"message": f"Product with product_id {product_id} not found."}), 404


def product_delete_by_id(product_id)
 global product_records
  for product in product_records:
       if product['product_id'] == product_id:
            product_records = [p for p in product_records if p['product_id'] != product_id]
            return jsonify({"message": f"Product with product_id {product_id} has been deleted."}), 200
        return jsonify({"message": f"Product with product_id {product_id} not found."}), 404


def get_all_products():
    return jsonify({"message": "Products retrieved", "results": product_records}), 200


def get_active_products():
    active_products = [p for p in product_records if p['active']]
    return jsonify({"message": "Active products retrieved", "results": active_products}), 200


def update_product_activity(request, product_id):
    data = request.form if request.form else request.get_json()
    active_status = data.get('active')

    if active_status is None:
        return jsonify({"massage": "Active statis is required."}), 400

    for product in product_records:
        if product['product_id'] == product_id:
            product['active'] = active_status
            return jsonify({"message": f"Product {product['product_name']} active status has been updated."}), 200
    return jsonify({"message": f"Product with product_id {product_id} not fount."}), 404
