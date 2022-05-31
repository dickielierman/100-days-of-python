from turtle import Turtle, Screen, colormode
import random
from color_list import my_colors as mc


def walk_dots():

    for i in range(10):
        for _ in range(10):
            this_color = rand_color()
            h.pendown()
            h.dot(20,this_color)
            h.penup()
            if _ != 9:
                h.forward(50)
        if i != 9:
            h.setheading(90)
            h.forward(50)
            h.setheading(180)
            h.forward(50*9)
            h.setheading(0)
        else:
            h.color(this_color)


def rand_color():
    return random.choice(mc)


h = Turtle()
colormode(255)
h.shape('arrow')
h.speed(0)
h.pensize(20)
h.penup()
h.back(50*5)
h.setheading(270)
h.forward(50*5)
h.setheading(0)
walk_dots()
screen = Screen()
screen.exitonclick()