from turtle import Screen, Turtle
ALIGN = "center"
screen = Screen()
MYFONT = ('Courier', 24, 'bold')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.hideturtle()
        self.color('white')
        self.goto(0, 265)
        self.print_score()

    def print_score(self):
        self.write(f"Current Score: {self.score}", align=ALIGN, font=MYFONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.print_score()

    def game_over(self, extra_text=''):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=MYFONT)
        if extra_text != '':
            self.goto(0, -40)
            self.write(f"{extra_text}", align=ALIGN, font=MYFONT)
        return screen.textinput(title="Play again", prompt="Would you like to play again? 'y' or 'n'").lower()
