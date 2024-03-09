from turtle import Turtle, Screen
from random import randint

turtle_color = ["orange", "blue", "green", "pink", "black", "red"]
turtle_list = []

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter color: ")

y_position = -100
for _ in range(len(turtle_color)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(turtle_color[_])
    new_turtle.goto(-230, y_position)
    y_position += 40
    turtle_list.append(new_turtle)


is_race_one = True

while is_race_one:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_one = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won. The color of the winning turtle is {winning_turtle} ")
            else:
                print(f"You've lost. The color of the winning turtle is {winning_turtle} ")

        turtle.forward(randint(0,10))

screen.exitonclick()