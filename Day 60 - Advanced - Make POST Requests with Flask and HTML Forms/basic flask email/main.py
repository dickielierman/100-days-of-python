from flask import Flask, render_template, request
import requests as req
app = Flask(__name__)
from datetime import datetime as dt
copycode = f'Copyright © Dickie Lierman {dt.now().year}'

@app.route('/')
def home():
    return render_template("index.html", copycode=copycode,)

@app.route('/login', methods=["POST"])
def receive_data():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username,password)

    else:
        error = 'Invalid username/password'

    return render_template("index.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)