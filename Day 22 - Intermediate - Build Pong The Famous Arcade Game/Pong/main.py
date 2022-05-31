# create class for scoreboard

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# create court class

from turtle import Screen, Turtle
import time

# paddle = Paddle()
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pongish")
screen.tracer(0)


right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
playing = True

while playing:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detect collision with r paddle
    if ball.xcor() > 325 and ball.distance(right_paddle) <= 50 or ball.xcor() < -325 and ball.distance(left_paddle) <= 50:
        ball.hit()

    # detect misses
    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset()
    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset()

screen.exitonclick()
