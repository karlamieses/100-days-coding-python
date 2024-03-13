from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.user_score = 0
        self.goto(0, 260)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.user_score}", move=False, align=ALIGNMENT, font=FONT)

    def is_game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=FONT)

    def increase_score(self):
        self.user_score += 1
        self.clear()
        self.update_score()





