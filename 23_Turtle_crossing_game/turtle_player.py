from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('red')
        self.left(90)
        self.penup()
        self.goto(0, -260)

    def forward_turtle(self):
        self.forward(10)

    def backward_turtle(self):
        self.backward(10)

    def level_up(self):
        self.hideturtle()
        self.goto(0, -260)
        self.showturtle()
