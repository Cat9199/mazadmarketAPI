from app.models import db, Product, ProductImg, ProductVideos,User
from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta  
import jwt

Product_bp = Blueprint('product', __name__)



@Product_bp.route('/products', methods=['GET'])
def list_products():
      products = Product.query.filter_by(is_active=True).order_by(Product.id.desc()).limit(100).all()
      # Get all products img and retern a object for all spesefec prodect with her imges and product deteles


@Product_bp.route('/products/<int:product_id>', methods=['GET'])
def product_detail(product_id):
      product = Product.query.filter_by(id=product_id, is_active=True).first()
      if not product:
            return jsonify({'message': 'Product not found'}), 404
      return jsonify({'product': product.to_dict()})

@Product_bp.route('/upload_image', methods=['POST'])
def upload_image():
      if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

      file = request.files['file']
      m
      if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
     # Save the file to the database
      img = ProductImg(Img=file.read())
      db.session.add(img)
      db.session.commit()
      return jsonify({'message': 'Image uploaded successfully'}), 200

@Product_bp.route('/img/<int:img_id>', methods=['GET'])
def img_detail(img_id):
      img = ProductImg.query.filter_by(id=img_id).first()
      if not img:
            return jsonify({'message': 'Image not found'}), 404
      return Response(img.Img, mimetype='image/jpeg')