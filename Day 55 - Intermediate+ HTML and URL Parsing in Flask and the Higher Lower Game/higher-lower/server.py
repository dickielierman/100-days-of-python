# Now it's time to complete the final project of the day, the higher lower game that we created in Day 14, but now with a real website.
#
# 1. Create a new project in PyCharm called higher-lower, add a server.py file.
#
# 2. Create a new Flask application where the home route displays an <h1> that says "Guess a number between 0 and 9" and display a gif of your choice from giphy.com.
#
# Alternatively use the one I found on Giphy: https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif
#
#
# 3. Generate a random number between 0 and 9 or any range of numbers of your choice.
#
# 4. Create a route that can detect the number entered by the user e.g "URL/3" or "URL/9" and checks that number against the generated random number. If the number is too low, tell the user it's too low, same with too high or if they found the correct number. try to make the <h1> text a different colour for each page.  e.g. If the random number was 5:
#
# 3 is too low:
#
#
#
# 7 is too high:
#
#
# and 5 is just right:
#
#
# Here are the GIF URLs I used, but it's way more fun finding your own on giphy.com
#
# High: https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif
#
# Low: https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif
#
# Correct: https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif

from flask import Flask
from random import randint
app = Flask(__name__)

secret_number = randint(1, 10)

results = {
    "correct": {"style": "color: green;", "gif": "https://media.giphy.com/media/U4DswrBiaz0p67ZweH/giphy.gif"},
    "too_high": {"style": "color: red;", "gif": "https://media.giphy.com/media/wHB67Zkr63UP7RWJsj/giphy.gif"},
    "too_low": {"style": "color: blue;", "gif": "https://media.giphy.com/media/GIvajz0TlE316/giphy.gif"}
}

def check_answer(function):
    def wrapper(*args, **kwargs):
        if kwargs['user_number'] == secret_number:
            res = 'correct'
        elif kwargs['user_number'] > secret_number:
            res = 'too_high'
        else:
            res = 'too_low'
        return f"<div style='text-align: center;'>" \
               f"<h1 style='{results[res]['style']}'>{function(kwargs['user_number'])} {res.replace('_', ' ')}!</h1>" \
               f"<img src='{results[res]['gif']}' atl='{res.replace('_', ' ').title()}'>" \
               f"</div>"

    return wrapper


def wrap_div(function):
    def div_wrapper(*a, **k):
        return f'<div style="text-align: center;">{function(*a, **k)}</div>'
    return div_wrapper


@app.route('/')
@wrap_div
def hello_world():
    secret_number = randint(1, 10)
    return "<h1>Choose a number between 1 and 10</h1>" \
           "<img src='https://media.giphy.com/media/UDU4oUJIHDJgQ/giphy.gif' atl='Choose a random number'>"


@app.route('/<int:user_number>')
@check_answer
def user_guess(user_number):
    return f"You are"


if __name__ == "__main__":
    app.run(debug=True)