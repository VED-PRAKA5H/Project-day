from turtle import Turtle
FONT = ('futura', 40, 'normal')


class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.color('white')
        self.x = 0
        self.l = 0
        self.score_l()
        self.score_r()

    def score_l(self):
        """live scoreboard of user"""
        self.clear()
        self.write(f" {self.l} ", False, "center", FONT)
        self.l += 1

    def score_r(self):
        self.clear()
        self.write(f" {self.x} ", False, "center", FONT)
        self.x += 1
