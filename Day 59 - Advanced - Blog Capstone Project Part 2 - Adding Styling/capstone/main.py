from flask import Flask, render_template
import requests as req
from post import Post
app = Flask(__name__)
from datetime import datetime as dt

copycode = f'Copyright © Dickie Lierman {dt.now().year}'

posts = req.get(f'https://api.npoint.io/8e0f8745a060237bb237').json()
post_objects = [Post(post["id"], post["author"], post["date"], post["title"], post["subtitle"], post["body"], post["image"]) for post in posts]



@app.route('/')
def home():
    return render_template("index.html", copycode=copycode, blog=post_objects)


@app.route('/post/<int:blog_id>')
def post(blog_id):
    for blog_post in post_objects:
        if blog_post.id == blog_id:
            req_post = blog_post
    return render_template("post.html", copycode=copycode, blog=req_post)

@app.route('/about')
def about():
    return render_template("about.html", copycode=copycode)

@app.route('/contact-me')
def contact():
    return render_template("contact.html", copycode=copycode)


if __name__ == "__main__":
    app.run(debug=True)
