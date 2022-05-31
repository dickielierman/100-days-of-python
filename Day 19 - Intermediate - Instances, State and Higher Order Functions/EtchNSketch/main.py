from turtle import Turtle, Screen, colormode
import random


def move_forward():
    eas.forward(10)


def move_backward():
    eas.back(10)


def turn_left():
    eas.left(10)


def turn_right():
    eas.right(10)


def clear():
    eas.clear()
    eas.penup()
    eas.goto(0,0)
    eas.pendown()


eas = Turtle()
eas.shape('arrow')
eas.speed(0)
screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
