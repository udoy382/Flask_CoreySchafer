from flask import Flask, render_template, url_for, flash, redirect, request
from flask_blog import app, db, bcrypt
from flask_blog.forms import LoginForm, UpdateAccountForm
from flask_blog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date': 'January 7 2022'
    },
    {
        'author': 'Udoy',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date': 'January 5 2022'
    }
]

@app.route('/')
def home():
    # return '<h1>Home page</h1>'

    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    # return '<h1>About page</h1>'

    return render_template('about.html', title='heyabout')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()

        flash('Your account has been created! You are now able to login' 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)



# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     return render_template('register.html', title='Login', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    form = UpdateAccountForm()
    image_file = url_for('static', filename='udoy.png' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)