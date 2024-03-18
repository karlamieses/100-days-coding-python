from turtle import Turtle

STARTING_POINT = (0, -270)
TURTLE_MOVING_DISTANCE = 20


class TurtlePlayer(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POINT)
        self.setheading(90)

    def move_up(self):
        self.forward(TURTLE_MOVING_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POINT)
