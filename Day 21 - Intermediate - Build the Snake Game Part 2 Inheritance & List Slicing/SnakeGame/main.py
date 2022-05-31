from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake


def snake_game():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    playing = True
    while playing:
        screen.update()
        time.sleep(.1)
        snake.move()

        # detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.add_score()
        # detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            playing = False
            if scoreboard.game_over("You collided with the wall.") == 'y':
                screen.resetscreen()
                snake_game()
        # detect collision with tail
        for segment in snake.body[1:]:
            if snake.head.distance(segment) < 10:
                playing = False
                if scoreboard.game_over("You collided with your tail.") == 'y':
                    screen.resetscreen()
                    snake_game()

snake_game()

