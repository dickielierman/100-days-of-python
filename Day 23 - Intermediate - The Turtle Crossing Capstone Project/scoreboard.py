from turtle import Turtle
FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()

        self.display()

    def display(self):
        self.clear()
        self.goto(-283,258)
        self.color('black')
        self.write('Level: ' + str(self.level), False, align="left", font=FONT)
        self.goto(-285,260)
        self.color('white')
        self.write('Level: ' + str(self.level), False, align="left", font=FONT)

    def you_lose(self):
        self.goto(0, 0)
        self.color('black')
        self.write('YOU LOSE AT LEVEL: ' + str(self.level), False, align="center", font=FONT)