import json
import os
from flask_sqlalchemy import SQLAlchemy
from MarketPlace.api import app

baseDir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(baseDir, 'MarketPlace.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialise Database
db = SQLAlchemy(app)



class Product(db.Model):
    __tablename__ = 'products'
    ProductCode = db.Column(db.String(10), primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Price = db.Column(db.Float, nullable=False)

    def json(self):
        return {"ProductCode":self.ProductCode,"Name": self.Name,"Price": self.Price}

    def add_product(self,_productCode, _name, _price):
        new_product = Product(ProductCode=_productCode, Name=_name, Price=_price)
        try:
            db.session.add(new_product)
            db.session.commit()
        except Exception as e :
            print(e)
            db.session.rollback()

    def get_all_products(self):
        return [Product.json(product) for product in Product.query.order_by('ProductCode').all()]

    def get_product(self,_productCode):
        if Product.query.filter_by(ProductCode=_productCode).first():
            return Product.json(Product.query.filter_by(ProductCode=_productCode).first())
        else:
            None
        #return Product.query.filter_by(ProductCode=_productCode).first()

    def update_product(self,_productCode, _name, _price):
        updatedProduct = Product.query.filter_by(ProductCode=_productCode).first()
        updatedProduct.Name = _name
        updatedProduct.Price = _price

        db.session.commit()

    def update_product_price(self,_productCode,_price):
        updatedProduct = Product.query.filter_by(ProductCode=_productCode).first()
        updatedProduct.Price = _price
        db.session.commit()

    def delete_product(self, _productCode):
        Product.query.filter_by(ProductCode=_productCode).delete()
        db.session.commit()

    def __repr__(self):
        Product_Object = {
            'ProductCode':self.ProductCode,
            'Name' : self.Name,
            'Price' :  self.Price
        }
        return json.dumps(Product_Object)

    def validProduct(self,productObject):
        if 'ProductCode' in productObject and 'Price' in productObject and 'Name' in productObject:
            return True
        else:
            return False