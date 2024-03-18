from turtle import Screen
from turtle_player import TurtlePlayer
from car_manager import Cars
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
screen.tracer(0)

scoreboard = Scoreboard()
turtle_player = TurtlePlayer()

new_cars = []
cars = Cars()
new_cars.append(cars)

screen.listen()
screen.title("Python Turtle Graphics")
screen.setup(width=600, height=600)

screen.onkey(fun=turtle_player.move_up, key="Up")

is_game_on = True

while is_game_on:
    sleep(scoreboard.game_speed)
    screen.update()

    for car in new_cars:
        car.forward(-20)

    # Print two new cars starting on the right when xcor == 180.
    if new_cars[-1].xcor() == 180:
        for _ in range(2):
            cars = Cars()
            new_cars.append(cars)

    # Detect when the user passed the level
    if turtle_player.ycor() > 280:
        scoreboard.update_level()
        turtle_player.reset_position()

    # Detect turtle collapsing with car.
    for car in new_cars:
        if turtle_player.distance(car) < 20:
            scoreboard.game_over()
            is_game_on = False

screen.exitonclick()
