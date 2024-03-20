from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

print(scoreboard.user_score)
is_game_on = True
while is_game_on:
    screen.update()
    sleep(0.2)
    snake.move()

    # Detect collision with Food.
    if snake.snake_head.distance(food) < 15:
        food.refresh_food_coordinates()
        scoreboard.increase_score()
        snake.extend_snake()
    # Detect collision with Wall.
    if snake.snake_head.xcor() < -280 or snake.snake_head.xcor() > 280 or snake.snake_head.ycor() < -280 or snake.snake_head.ycor() > 280:
        scoreboard.reset_score()
        snake.reset_snake()

    # Detect collision with Snake.
    # In here we are not taking into account the first position as automatically this fails the code
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.reset_score()


screen.exitonclick()
