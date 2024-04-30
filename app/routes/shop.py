from flask import Blueprint

shop_bp = Blueprint('shop', __name__)

@shop_bp.route('/products')
def list_products():
        return "List of Products"

@shop_bp.route('/products/<int:product_id>')
def product_detail(product_id):
        return f"Details for product {product_id}"
