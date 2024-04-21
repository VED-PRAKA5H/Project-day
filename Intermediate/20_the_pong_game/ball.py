from turtle import Turtle


class Dot(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(.8)
        self.penup()
        self.x = 10
        self.y = 10
        self.setheading(0)
        self.color('purple')

    def move1(self, y):
        self.goto(300, y=y)
        self.goto(-300, y=y)

    def move_forward(self):
        self.goto(self.xcor()+self.x, self.ycor()+self.y)

    def y_bounce(self):
        self.y *= -1

    def x_bounce(self):
        self.x *= -1
