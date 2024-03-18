from turtle import Turtle

FONT = ("Courier", 25, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.hideturtle()
        self.penup()
        self.goto(-210, 250)
        self.level = 1
        self.game_speed = 0.5
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)
        self.level += 1
        self.game_speed *= 0.9

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)

