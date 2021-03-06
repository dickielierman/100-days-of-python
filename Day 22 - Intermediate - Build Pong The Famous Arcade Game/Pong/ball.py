from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self, pos=(350, 0)):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.hit()
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()
        time.sleep(1)
        self.move_speed = 0.1
        self.move()
