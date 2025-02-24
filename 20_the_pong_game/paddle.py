from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.shape('square')
        self.penup()
        self.goto(x, y)
        self.turtlesize(1, 5)
        self.right(90)
        self.color('white')
        self.showturtle()

    def down(self):
        self.backward(30)

    def up(self):
        self.forward(30)

