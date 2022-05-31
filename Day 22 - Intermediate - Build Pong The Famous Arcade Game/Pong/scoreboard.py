from turtle import Turtle

ALIGN = "center"
MYFONT = ('Courier', 40, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-40, 220)
        self.write(self.l_score, align=ALIGN, font=MYFONT)
        self.goto(40, 220)
        self.write(self.r_score, align=ALIGN, font=MYFONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
