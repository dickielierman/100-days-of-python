from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
ckeditor = CKEditor(app)
Bootstrap5(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

def get_formatted_date():
    current_date = datetime.now()
    formatted_date = current_date.strftime('%B %d, %Y')
    return formatted_date

with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():

    with db.session.begin():
        result = db.session.execute(db.select(BlogPost))
        all_posts = result.scalars().all()
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = [post for post in all_posts]
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/show_post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = BlogPost.query.get(post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = CreatePostForm()
    if request.method == "POST" and form.validate_on_submit():
        title = form.title.data
        subtitle = form.subtitle.data
        date_right_now = get_formatted_date()
        author = form.author.data
        img_url = form.img_url.data
        body = form.body.data


        new_post = BlogPost(
            title = title,
            subtitle = subtitle,
            date = date_right_now,
            author = author,
            img_url = img_url,
            body = body,
        )
        try:
            with db.session.begin():
                db.session.add(new_post)
            return redirect(url_for('get_all_posts'))
        except Exception as e:
            db.session.rollback()

    return render_template("make-post.html", form=form)




# TODO: edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    edit_form = CreatePostForm(title=post.title,
    subtitle=post.subtitle,
    img_url=post.img_url,
    author=post.author,
    body=post.body)

    if request.method == "POST" and edit_form.validate_on_submit():
        title = edit_form.title.data
        subtitle = edit_form.subtitle.data
        author = edit_form.author.data
        img_url = edit_form.img_url.data
        body = edit_form.body.data

        if post.title != edit_form.title.data:
            post.title = edit_form.title.data
        if post.subtitle != edit_form.subtitle.data:
            post.subtitle = edit_form.subtitle.data
        if post.author != edit_form.author.data:
            post.author = edit_form.author.data
        if post.img_url != edit_form.img_url.data:
            post.img_url = edit_form.img_url.data
        if post.body != edit_form.body.data:
            post.body = edit_form.body.data

        try:
            # Save changes to the database
            db.session.commit()
            return redirect(url_for('show_post', post_id=post_id))
        except Exception as e:
            db.session.rollback()



    return render_template("make-post.html", form=edit_form, is_edit=True)




# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>", methods=["GET", "POST", "PUT"])
def delete_post(post_id):
    try:
        BlogPost.query.filter_by(id=post_id).delete()
        db.session.commit()

    except:
        db.session.rollback()
    return redirect(url_for('get_all_posts'))
# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
