from flask import Flask


def make_bold(function):
    def bolded(*args, **kwargs):
        return "<b>" + function(*args, **kwargs) + "</b>"

    return bolded


def make_emphasis(function):
    def emphasis(*args, **kwargs):
        return "<em>" + function(*args, **kwargs) + "</em>"

    return emphasis


def make_underlined(function):
    def underlined(*args, **kwargs):
        return "<u>" + function(*args, **kwargs) + "</u>"

    return underlined


def make_home_link(function):
    def home_link(*args, **kwargs):
        return "<a href='/'>" + function(*args, **kwargs) + "</a>"

    return home_link


app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<a href='/bye'>Hello, World!</a><br><a href='/username/dickie'>User name</a>"


@app.route('/bye')
@make_home_link
@make_emphasis
@make_bold
def goodbye_world():
    return "Goodbye, Cruel World!"


@app.route('/username/<name>')
@make_bold
def hey_name(name):
    return f"hey {name}!"


if __name__ == "__main__":
    app.run(debug=True)
