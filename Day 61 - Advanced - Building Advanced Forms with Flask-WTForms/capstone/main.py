from flask import Flask, render_template, request
import requests as req
from post import Post
app = Flask(__name__)
from message import Message
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


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    result = {}
    if request.method == 'POST':
        name = request.form['name'].strip()
        email = request.form['email'].strip()
        phone = request.form['phone'].strip()
        message = request.form['message'].strip()
        result['data'] = {"name": name, "email": email, "phone": phone, "message": message}
        if name == '' or email == '' or phone == '' or message == '':
            errorlist = []
            if name == '':
                errorlist.append("name")
            if email == '':
                errorlist.append("email")
            if phone == '':
                errorlist.append("phone")
            if message == '':
                errorlist.append("message")
            result['error'] = f'Invalid or missing Information: {", ".join(errorlist)}'
            return render_template("contact.html", _anchor='submitErrorMessage', copycode=copycode, result=result)
        else:
            m = Message(name, email, phone, message)
            m.send_mail()
            result['data'] = {"name": '', "email": '', "phone": '', "message": ''}
            result['success'] = 'Message Sent'
            return render_template("contact.html", _anchor='submitSuccessMessage', copycode=copycode, result=result)
    else:
        result['data'] = {"name": '', "email": '', "phone": '', "message": ''}
        return render_template("contact.html", copycode=copycode , result=result)


if __name__ == "__main__":
    app.run(debug=True)
