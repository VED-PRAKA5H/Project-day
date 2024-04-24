from turtle import Turtle
FONT = ("Ariel", 20, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(250, 280)
        self.score = 0
        self.show_score(self.score, 0)

    def show_score(self, score, time):
        self.clear()
        self.write(f"score: {score}/36\nRemaining time: {int((5*60-time) / 60)}:{"{:02d}".format(int(60-time % 60))}", align='right', font=FONT)
