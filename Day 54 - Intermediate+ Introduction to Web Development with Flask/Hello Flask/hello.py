from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<a href='/bye'>Hello, World!</a>"

@app.route('/bye')
def goodbye_world():
    return "Goodbye, Cruel World!"


if __name__ == "__main__":
    app.run()