from turtle import Screen
import time
from cars import Car
from scoreboard import Score
from turtle_player import Player

# setup screen
screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.setup(800, 600)

# Create game objects
score = Score()
my_turtle = Player()

# Configure screen to listen for key presses
screen.listen()
screen.onkey(my_turtle.forward_turtle, 'Up')
screen.onkey(my_turtle.backward_turtle, 'Down')

# Initialize game variables
count = 0
sleep_time = 0.1
game_is_on = True
cars = []

# Game loop
while game_is_on:
    time.sleep(sleep_time)
    screen.update()

    # Check for collision with cars
    for j in range(len(cars)):
        if my_turtle.distance(cars[j]) <= 22:
            score.hit()
            game_is_on = False

    # Generate new cars at intervals
    if count % 20 == 0:
        for i in range(5):
            car = Car()
            cars.append(car)

    # Move cars and increment count
    for i in range(len(cars)):
        cars[i].move_left()
    count += 1

    # Check for level up
    if my_turtle.ycor() > 270:
        sleep_time *= 0.8
        score.score()
        my_turtle.level_up()

# Close the game window on click
screen.exitonclick()
