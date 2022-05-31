from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.total_states = 50
        self.correct_guess_count = 0
        self.shape('square')
        self.hideturtle()
        self.penup()
        self.correct_guesses =[]

    def add_state(self, state, x, y):
        self.goto(x, y)
        self.write(state)
        self.correct_guess_count += 1
        self.correct_guesses.append(state)