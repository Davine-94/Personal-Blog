from flask import render_template, request, Blueprint
import json
import requests
from app.models import Post

main = Blueprint('main',__name__)

@main.route("/", methods = ['GET'])
def home():
    title = 'Daily Dose of Inspiration'
    req = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    data= json.loads(req.content)
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template("index.html", title=title, posts=posts, data= data)