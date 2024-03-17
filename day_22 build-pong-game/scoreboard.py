from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=self.left_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(arg=self.right_score, align="center", font=("Courier", 80, "normal"))

    def left_points(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_points(self):
        self.right_score += 1
        self.update_scoreboard()
