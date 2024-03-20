from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.user_score = 0
        with open("scoreboard_data.rtf", mode="r") as score_data:
            self.high_score = int(score_data.read())
        self.goto(0, 260)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.user_score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.user_score > self.high_score:
            self.high_score = self.user_score
            with open("scoreboard_data.rtf", mode="w") as score_data:
                score_data.write(f"{self.high_score}")

        self.user_score = 0
        self.update_score()

    def increase_score(self):
        self.user_score += 1
        self.update_score()
