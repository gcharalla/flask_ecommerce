from market import db
from market import app


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(length=30), nullable=False, unique=True)
    stock = db.Column(db.Integer(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    img = db.Column(db.String(length=100), nullable=False)


with app.app_context():
    db.create_all()
