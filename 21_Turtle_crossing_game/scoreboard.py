from turtle import Turtle
FONT = ('Arial', 20, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-340, 240)
        self.x = 1
        self.color('white')
        self.score()

    def score(self):
        self.clear()
        self.write(f"Level: {self.x}", move=False, align='center', font=FONT)
        self.x += 1

    def hit(self):
        self.home()
        self.write(f"Game Over", move=False, align='center', font=FONT)
