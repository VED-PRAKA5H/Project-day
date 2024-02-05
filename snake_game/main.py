import time
from snake import Snake
from food import Food
from turtle import Screen
from increase_length import IncreaseLength
from score_board import Score
my_screen = Screen()
my_screen.bgcolor('gray20')
my_screen.setup(width=750, height=750)
my_screen.title("My Snake Game")
my_screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
increase = IncreaseLength()              # this increase length and checks collision with tail
score.score(snake.length)

my_screen.listen()
my_screen.onkey(snake.right, 'Right')
my_screen.onkey(fun=snake.left, key='Left')
my_screen.onkey(fun=snake.up, key='Up')
my_screen.onkey(fun=snake.down, key='Down')

while abs(snake.headposition[0]) <= 375 and abs(snake.headposition[1]) <= 375 and increase.is_game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()
    if int(abs(food.foodposition - snake.headposition)) == 0:
        food.create_food()
        increase.add_segment(snake.taildirection, snake.tailposition, snake.length, snake.my_turtles)
        snake.length = snake.length + 1
        score.score(snake.length)
    increase.tail_collision(snake.headposition, snake.my_turtles)

score.game_over()
my_screen.exitonclick()
