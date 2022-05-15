from flask import render_template
from app import app
from app.forms import RegistrationForm, LoginForm

app.config['SECRET_KEY'] = 'd41015350b40aadac73a9253ae9659bd'

@app.route("/")
def home():
    title = 'Daily Dose of Inspiration'
    return render_template("index.html", title=title)

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)