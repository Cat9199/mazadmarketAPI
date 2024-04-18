from flask import Flask, request, jsonify, make_response , Response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()



def create_app():
          app = Flask(__name__)
          app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
          app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
          app.config['SECRET_KEY'] ='MazadMarketSecretKey'
          app.config['API_URL'] = 'http://api.mazadmarket.com'
          app.config['API_VERSION'] = 'v1'
          app.config['API_NAME'] = 'mazadmarket'
          db.init_app(app)
          migrate.init_app(app, db)
          jwt = JWTManager(app)
          mail = Mail(app)
          # allow cross origin requests for all routes
          CORS(app, resources={r"/api/*": {"origins": "*"}})

          with app.app_context():
                        db.create_all()
          from .routes.auth import auth_bp
          from .routes.admin import admin_bp
          from .routes.shop import shop_bp
          from .routes.main import main_bp

          app.register_blueprint(auth_bp, url_prefix='/api/auth')
          app.register_blueprint(admin_bp, url_prefix='/admin')
          app.register_blueprint(shop_bp, url_prefix='/shop')
          app.register_blueprint(main_bp)
          return app
