from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, static_folder='static', static_url_path='/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'MazadMarketSecretKey'
    app.config['API_URL'] = 'http://api.mazadmarket.com'
    app.config['API_VERSION'] = 'v1'
    app.config['API_NAME'] = 'mazadmarket'
    
    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt = JWTManager(app)
    mail = Mail(app)

    # Enable CORS
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Create database tables
    with app.app_context():
        db.create_all()

    # Import and register blueprints
    from app.routes.auth import auth_bp
    from app.routes.admin import admin_bp
    from app.routes.shop import shop_bp
    from app.routes.main import main_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(shop_bp, url_prefix='/shop')
    app.register_blueprint(main_bp)

    return app
