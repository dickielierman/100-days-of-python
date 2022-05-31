from turtle import Turtle, Screen, colormode
import random


def move_forward():
    t.forward(10)


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

starting_y = -120
starting_x = -390
ending_x = 385
is_race_on = False
screen = Screen()
screen.setup(width=800,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Pick a color").lower()
all_turtles = []
winner = ''
for color in colors:
    t = Turtle(shape="turtle", visible=False)
    t.color(color)
    t.speed(0)
    t.pu()
    t.goto(x=starting_x, y=starting_y)
    t.showturtle()
    starting_y += 50
    all_turtles.append(t)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= ending_x:
            winner = turtle.pencolor()
            is_race_on = False
            break
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)

if winner == user_bet:
    print(f"Awesome! You won by betting on {winner}!")
else:
    print(f"Oh well! Your bet {user_bet} lost to {winner}.")


screen.exitonclick()
