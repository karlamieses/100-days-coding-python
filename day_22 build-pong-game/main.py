from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
screen.title("Pong")
screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()

scoreboard = Scoreboard()

left_paddle = Paddle(x_cord=-350)
right_paddle = Paddle(x_cord=350)

screen.onkey(fun=right_paddle.go_up, key="Up")
screen.onkey(fun=right_paddle.go_down, key="Down")
screen.onkey(fun=left_paddle.go_up, key="w")
screen.onkey(fun=left_paddle.go_down, key="s")

is_game_on = True
ball = Ball()

while is_game_on:
    sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_ball_position()
        scoreboard.left_points()

    # Detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_ball_position()
        scoreboard.right_points()

screen.update()
screen.exitonclick()
