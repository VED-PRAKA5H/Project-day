import turtle
from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape('circle')
        self.penup()
        self.color('red')
        self.foodposition = turtle.Vec2D(0, 80)
        self.create_food()

    def create_food(self):
        """creates food at any random position"""
        self.foodposition = (20*random.randint(-17, 17), 20*random.randint(-17, 17))
        self.goto(self.foodposition)
        self.showturtle()
        self.foodposition = self.pos()
        self.dot(1, "green")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
