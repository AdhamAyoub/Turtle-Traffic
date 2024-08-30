import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_car()


    # collides with car
    for car in cars.all_cars:
        if player.distance(car) < 28:
            game_is_on = False
            score.game_over()


    if player.ycor() > 287:
        player.goto_start()
        cars.increment_speed()
        score.level_up()

screen.exitonclick()
