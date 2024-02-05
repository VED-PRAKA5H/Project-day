import turtle
from turtle import Turtle
N = 3


class Snake:
    def __init__(self):
        self.my_turtles = []
        self.create_snake()
        self.headposition = turtle.Vec2D(0, 0)
        self.headdirection = 0
        self.tailposition = 0
        self.length = N
        self.taildirection = 0

    def create_snake(self):
        for i in range(N):
            self.my_turtles.append('my_turtle'+str(i+1))
            self.my_turtles[i] = Turtle(shape='square')
            self.my_turtles[i].color('aliceblue')
            self.my_turtles[i].penup()
            self.my_turtles[i].setposition(x=i*20, y=0)
        self.my_turtles[N-1].color('red')

    def right(self):
        if self.headdirection % 180 != 0:
            self.my_turtles[self.length - 1].setheading(0)

    def left(self):
        if (self.headdirection-180) % 180 != 0:
            self.my_turtles[self.length - 1].setheading(180)

    def up(self):
        if (self.headdirection - 90) % 180 != 0:
            self.my_turtles[self.length - 1].setheading(90)

    def down(self):
        if (self.headdirection - 270) % 180 != 0:
            self.my_turtles[self.length - 1].setheading(270)

    def move(self):
        """moves snake and contains record of positions of snake's head and tail"""
        for j in range(self.length - 1):
            x = self.my_turtles[j + 1].xcor()
            y = self.my_turtles[j + 1].ycor()
            self.headdirection = self.my_turtles[j + 1].heading()
            self.my_turtles[j].setheading(self.headdirection)
            self.my_turtles[j].goto(x, y)

        self.my_turtles[self.length - 1].forward(20)
        tailpos = self.my_turtles[0].pos()
        headpos = self.my_turtles[self.length-1].pos()
        self.headposition = headpos
        self.tailposition = tailpos
        self.taildirection = self.my_turtles[self.length - 1].heading()
