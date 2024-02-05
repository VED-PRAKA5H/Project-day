from turtle import Turtle
FONT = ('futura', 15, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 351)
        self.color('white')

    def score(self, length):
        """live scoreboard of user"""
        self.clear()
        self.write(f"SCORE: {length - 3} ", False, "center", FONT)

    def game_over(self):
        """game over when snake's head collide with wall or body parts"""
        self.home()
        self.write(f"GAME OVER", False, "center", FONT)







