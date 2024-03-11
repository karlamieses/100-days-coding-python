import turtle
from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.x_coordinate = 0
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        """Creates the segments of square that builds the snake"""
        for _ in range(3):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(self.x_coordinate, 0)
            self.x_coordinate -= 20
            self.segments.append(new_segment)

    def move(self):
        """This function takes the x and y coordinate of the last position of the segments until 0 (not inclusive)
            so the squares or segments follow each other and move like snakes
        """
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)

        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        """Rule, if snake is facing Up the snake cannot move Down"""
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        """Rule, if snake is facing Down the snake cannot move Up"""
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def right(self):
        """Rule, if snake is facing Right the snake cannot move Left"""
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def left(self):
        """Rule, if snake is facing Left the snake cannot move Right"""
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(LEFT)
