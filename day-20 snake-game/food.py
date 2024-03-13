from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.refresh_food_coordinates()

    def refresh_food_coordinates(self):
        x_coordinate = randint(-280, 280)
        y_coordinate = randint(-280, 280)
        self.goto(x_coordinate, y_coordinate)
