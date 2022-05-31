from turtle import Turtle, Screen, colormode
import random

directions = [0, 90, 180, 270]


def random_walk():
    color_tuple = (rand_color())
    tim.pencolor(color_tuple)
    tim.forward(30)
    tim.setheading(random.choice(directions))


def rand_color():
    tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return tup

def spirograph(amt):
    for i in range(int(360 / amt)):
        color_tuple = (rand_color())
        tim.pencolor(color_tuple)
        tim.speed(0)
        tim.circle(100)
        tim.setheading(tim.heading() + amt)
tim = Turtle()
colormode(255)
tim.shape('arrow')
spirograph(40)
spirograph(5)
spirograph(2)
screen = Screen()
screen.exitonclick()
