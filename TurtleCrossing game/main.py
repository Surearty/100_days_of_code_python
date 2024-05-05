import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()
screen.listen()
screen.onkey(player.move, "Up")
game_is_on = True
car_manager = CarManager()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
#detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
#detect collision with succes
    if player.got_finish():
        player.go_to_start()
        car_manager.level_up()

screen.exitonclick()
