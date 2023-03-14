from market import app
from flask import render_template, redirect, url_for, flash
from market import db
from market.models import Item, User
from market.forms import RegisterForm, LoginForm


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = db.session.execute(db.select(Item).order_by(Item.id)).scalars()
    return render_template('market.html', items=items)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        email_address=form.email_address.data,
                        password=form.password1.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:  # if there are not errors from the validations
        for err_msg in form.errors.values():
            flash(
                f'There was an error with creating a user: {err_msg}', category='danger')
            # print(f'There was an error with creating a user: {err_msg}')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()

    return render_template('login.html', form=form)
