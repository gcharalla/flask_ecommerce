from market import db
from market import app


class User (db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50),
                              nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(length=30), nullable=False, unique=True)
    stock = db.Column(db.Integer(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    img = db.Column(db.String(length=100), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))


""" with app.app_context():
    db.create_all()
    u1 = User(username='jsc', email_address='jsc@jsc', password_hash='123456')
    i1 = Item(title="MONITOR 25 ASUS ROG SWIFT PG259QNR FHD 360Hz", stock=10, price=650.00,
              img="https://cdn.memorykings.pe/files/2021/06/08/329196-MK029536A.jpg", owner=1)
    i2 = Item(title="MONITOR 27 ASUS BE279QSK IPS FHD con WebCam", stock=2, price=349.00,
              img="https://cdn.memorykings.pe/files/2022/03/24/336747-MK030991A.jpg", owner=1)
    db.session.add(u1)
    db.session.add(i1)
    db.session.add(i2)
    db.session.commit()
 """