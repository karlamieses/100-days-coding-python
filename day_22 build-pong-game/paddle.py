from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
# RIGHT = 0
# LEFT = 180


class Paddle(Turtle):

    def __init__(self, x_cord):
        super().__init__()
        self.x_coordinate_paddle = x_cord
        self.y_coordinate = 0
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=0.7)
        self.penup()
        self.goto(self.x_coordinate_paddle, self.y_coordinate)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.x_coordinate_paddle, new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.x_coordinate_paddle, new_y)

