from flask import Flask, render_template
import requests as req
from post import Post
app = Flask(__name__)
import os
from dotenv import load_dotenv
load_dotenv()
key = os.environ.get('NPOINTIO')
posts = req.get(f'https://api.npoint.io/{key}').json()
post_objects = [Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in posts]



@app.route('/')
def home():
    return render_template("index.html", blog=post_objects)


@app.route('/post/<int:blog_id>')
def post(blog_id):
    for blog_post in post_objects:
        if blog_post.id == blog_id:
            req_post = blog_post
    return render_template("post.html", blog=req_post)


if __name__ == "__main__":
    app.run(debug=True)
