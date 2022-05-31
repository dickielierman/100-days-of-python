import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from the_road import TheRoad

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
the_road = TheRoad()
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()
screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.you_lose()
            game_is_on = False
    if player.safe():
        scoreboard.level += 1
        scoreboard.display()
        player.return_to_start()
        car_manager.level_up()


screen.exitonclick()
