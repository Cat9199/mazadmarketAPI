from . import db

class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        password = db.Column(db.String(80), nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        account_type = db.Column(db.String(80))
        first_name = db.Column(db.String(80), nullable=False)
        last_name = db.Column(db.String(80), nullable=False)
        phone = db.Column(db.String(80), nullable=False)                
        address = db.Column(db.String(80), nullable=False)
        avatar = db.Column(db.String(80), nullable=False)
        loginType = db.Column(db.String(80), nullable=False)
        created_at = db.Column(db.DateTime, server_default=db.func.now())
        def serialize(self):
                          return {
                        'id': self.id,
                        'username': self.username,
                        'email': self.email,
                        'account_type': self.account_type,
                        'first_name': self.first_name,
                        'last_name': self.last_name,
                        'full_name': f'{self.first_name} {self.last_name}',
                        'phone': self.phone,
                        'address': self.address,
                        'loginType': self.loginType,
                        'avatar': self.avatar,
                        'created_at': self.created_at
                }
class Product(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(150), nullable=False)
        price = db.Column(db.Float, nullable=False)

        def __repr__(self):
                return f'<Product {self.name}>'
