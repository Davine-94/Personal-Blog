from flask import render_template
from app import app

@app.route("/")
def home():
    title = 'Daily Dose of Inspiration'
    return render_template("index.html", title=title)