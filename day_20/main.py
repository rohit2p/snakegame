from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# creating the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("MY SNAKE GAME")
screen.tracer(0)

Scoreboard = Scoreboard()
snake = Snake()
food = Food()

# setting key
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
# move forward 
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        Scoreboard.increase_score()

    #  detect collision with the food
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        Scoreboard.game_over()

    # detect collision with tail
    # if head collied with any segment in the tail
    # trigger game_over
    for Snake in snake.Snake[1:]:
        if snake.head.distance(Snake) < 10:
            game_is_on = False
            Scoreboard.game_over()

screen.exitonclick()
