from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# A secret key is required to use CSRF
app.config['SECRET_KEY'] = '60a805a16ed61b071052394d'
db.init_app(app)

from market import routes
from market import models