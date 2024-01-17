from flask import Flask, render_template
from datetime import datetime as dt
import random
import requests as req



COPYRIGHT_YEAR = dt.now().year

app = Flask(__name__)


@app.route('/')
def index_page():
    random_number = random.randint(1, 10)
    return render_template(
        'index.html',
        page_data={
            "number": random_number,
            "copyright_year": COPYRIGHT_YEAR
        }
    )


@app.route('/guess/<name>')
def guess_page(name):
    age_response = req.get(f'https://api.agify.io?name={name}').json()['age']
    gender_response = req.get(f'https://api.genderize.io?name={name}').json()['gender']
    return render_template(
        'guess.html',
        page_data={
            "name": name.title(),
            "gender": gender_response,
            "age": age_response,
            "copyright_year": COPYRIGHT_YEAR
        }
    )


@app.route('/blog')
def blog_page():
    blog = req.get(f'https://api.npoint.io/9c946fb7a2d5ce85db78').json()
    print(blog)
    return render_template(
        'blog.html',
        page_data={
            "blog": blog,
            "copyright_year": COPYRIGHT_YEAR
        }
    )
@app.route('/blog/<id>')
def single_blog_page(id):
    blog = req.get(f'https://api.npoint.io/9c946fb7a2d5ce85db78').json()
    return render_template(
        'blog.html',
        page_data={
            "blog": blog,
            "copyright_year": COPYRIGHT_YEAR,
            "blog_id": int(id)
        }
    )


if __name__ == '__main__':
    app.run(debug=True)