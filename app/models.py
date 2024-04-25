from . import db

class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        password = db.Column(db.String(80), nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
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
                        'first_name': self.first_name,
                        'last_name': self.last_name,
                        'full_name': f'{self.first_name} {self.last_name}',
                        'phone': self.phone,
                        'address': self.address,
                        'loginType': self.loginType,
                        'avatar': self.avatar,
                        'created_at': self.created_at
                }
class LoginTimes(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(120), nullable=False)
        login_time = db.Column(db.DateTime, nullable=False)
        device = db.Column(db.String(80), nullable=False)
        def serialize(self):
                return {
                        'id': self.id,
                        'email': self.email,
                        'login_time': self.login_time,
                        'device': self.device
                }


class Product(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(150), nullable=False)
        description = db.Column(db.String(10000), nullable=False)
        price = db.Column(db.Float, nullable=False)
        categoryId = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
        Barcode = db.Column(db.String(80), nullable=False)
        sellerEmail = db.Column(db.String(120), nullable=False)
        Condition = db.Column(db.String(80), nullable=False)
        Quantity = db.Column(db.Integer, nullable=True, default=1)
        DateListed = db.Column(db.DateTime, server_default=db.func.now())
        Dimensions = db.Column(db.String(100), nullable=True, default='100cmX100cm')
        Weight = db.Column(db.String(80), nullable=True, default='1kg')
        Manufacturer = db.Column(db.String(80), nullable=True, default='Unknown')
        ViewsCount = db.Column(db.Integer, nullable=True, default=0)
        IsActive = db.Column(db.Boolean, nullable=True, default=True)
        IsFeatured = db.Column(db.Boolean, nullable=True, default=False)
        SellerNotes = db.Column(db.String(1000), nullable=True)
        Tags = db.Column(db.String(1000), nullable=True)
        CustomerRatingAverage = db.Column(db.Float, nullable=True, default=0)
        NumberOfReviews = db.Column(db.Integer, nullable=True, default=0)
        SEOKeywords = db.Column(db.String(1000), nullable=True)
        def serialize(self):
                return {
                        'id': self.id,
                        'name': self.name,
                        'description': self.description,
                        'price': self.price,
                        'categoryId': self.categoryId,
                        'Barcode': self.Barcode,
                        'sellerEmail': self.sellerEmail,
                        'Condition': self.Condition,
                        'Quantity': self.Quantity,
                        'DateListed': self.DateListed,
                        'Dimensions': self.Dimensions,
                        'Weight': self.Weight,
                        'Manufacturer': self.Manufacturer,
                        'ViewsCount': self.ViewsCount,
                        'IsActive': self.IsActive,
                        'IsFeatured': self.IsFeatured,
                        'SellerNotes': self.SellerNotes,
                        'Tags': self.Tags,
                        'CustomerRatingAverage': self.CustomerRatingAverage,
                        'NumberOfReviews': self.NumberOfReviews,
                        'SEOKeywords': self.SEOKeywords
                }
class Category(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        ParentCategoryID = db.Column(db.Integer, nullable=True)
        Name = db.Column(db.String(150), nullable=False)
        Description = db.Column(db.String(10000), nullable=False)
        ImageURL = db.Column(db.String(1000), nullable=True)
        def serialize(self):
                return {
                        'id': self.id,
                        'ParentCategoryID': self.ParentCategoryID,
                        'Name': self.Name,
                        'Description': self.Description,
                        'ImageURL': self.ImageURL
                }

class ProductImg(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
        Img = db.Column(db.LargeBinary)

class ProductVideos(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
        VideoFilePath = db.Column(db.String(1000), nullable=False)

