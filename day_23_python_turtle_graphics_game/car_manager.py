from turtle import Turtle
from random import choice, randint

color = ["Blue", "Red", "Yellow", "Green", "Orange"]


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(choice(color))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(280, randint(-230, 230))
