from market import app
from flask import render_template
from market import db
from market.models import Item
from market.forms import RegisterForm


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = db.session.execute(db.select(Item).order_by(Item.id)).scalars()
    return render_template('market.html', items=items)


@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)
