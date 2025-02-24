import random
from turtle import Turtle
from random import randint
colors = ['white', 'green', 'yellow', 'blue', 'purple', 'navy', 'magenta']


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.shape('square')
        self.shapesize(1, 2)
        self.color(random.choice(colors))
        self.y = 20 * randint(-11, 11)
        self.x = 400 + 100*random.random()
        self.goto(self.x, self.y)

    def move_left(self):
        self.goto(self.xcor()-10, self.ycor())
