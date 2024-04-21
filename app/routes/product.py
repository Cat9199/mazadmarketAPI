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
      ProdeuctImg = ProductImg.query.filter_by(product_id=product_id).all()
      ProdeuctVideos = ProductVideos.query.filter_by(product_id=product_id).all()

      if not product:
            return jsonify({'message': 'Product not found'}), 404
      sefiexImgurl = f'{app.config.get('API_URL') }/api/product/img/'
      sefiexVideoUrl = f'{app.config.get('API_URL') }/api/product/video/'
      return jsonify({'product': product.to_dict(), 'img': [img.to_dict() for img in ProdeuctImg], 'video': [video.to_dict() for video in ProdeuctVideos],'sefiexImgurl': sefiexImgurl,'sefiexVideoUrl': sefiexVideoUrl}), 200

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
@Product_bp.route('/upload_video', methods=['POST'])

def upload_video():
      if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
        file = request.files['file']
      if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
            # Save the file to the database
            video = ProductVideos(Video=file.read())
            db.session.add(video)
            db.session.commit()
            return jsonify({'message': 'Video uploaded successfully'}), 200
            # return jsonify({'message': 'Image uploaded successfully'}), 200


@Product_bp.route('/video/<int:video_id>', methods=['GET'])\
def video_detail(video_id):
            video = ProductVideos.query.filter_by(id=video_id).first()
            if not video:
                  return jsonify({'message': 'Video not found'}), 404
            return Response(video.Video, mimetype='video/mp4')
