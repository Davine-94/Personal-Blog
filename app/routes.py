from flask import render_template, flash, redirect, url_for
from app import app
import json
import requests
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/", methods = ['GET'])
def home():
    title = 'Daily Dose of Inspiration'
    req = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    data= json.loads(req.content)
    return render_template("index.html", title=title, posts=posts, data= data)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@demo.com' and form.password.data == 'password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
    else:
        flash('Login Unsuccessful','danger')
    return render_template('login.html', title='Login', form=form)