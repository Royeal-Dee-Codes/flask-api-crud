from flask import request, Blueprint
from controllers.products_controller import product_create, product_get_by_id, product_update_by_id, product_delete_by_id, get_all_products, get_active_products,    update_product_activity

product = Blueprint('product', __name__)


@product.route('/product', methods=['POST'])
def product_add():
    return product_create(request)


@product.route('/product/<product_id>', methods=['GET'])
def get_product_by_id(product_id):
    return product_get_by_id(product_id)


@product.route('/product/<product_id>', methods=['PUT'])
def update_product_by_id(product_id):
    return product_update_by_id(request, product_id)


@product.route('/product/delete/<product_id>', methods=['DELETE'])
def delete_product_by_id(product_id):
    return product_delete_by_id(product_id)


@product.route('/products', methods=['GET'])
def get_all_products_route():
    return get_all_products()


@product.route('/products/active', methods=['GET'])
def get_active_products_route():
    return get_active_products()


@product.route('/product/activity/<product_id>', methods=['PATCH'])
def update_product_activity_route(product_id):
    return update_product_activity(request, product_id)
