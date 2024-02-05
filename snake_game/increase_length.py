from turtle import Turtle


class IncreaseLength:
    def __init__(self):
        self.is_game_on = True

    @staticmethod
    def add_segment(tail_direction, tail_position, length, my_turtles):
        """adds an segment i snake"""
        my_turtles.insert(0, ('my_turtle' + str(length)))
        my_turtles[0] = Turtle(shape='square')
        my_turtles[0].color('aliceblue')
        my_turtles[0].penup()
        my_turtles[0].setposition(tail_position)
        my_turtles[0].setheading(tail_direction)

    def tail_collision(self, head_position, my_turtles):
        """checks head collision with parts of snake"""
        for turtle in my_turtles[:len(my_turtles)-2]:
            if int(abs(head_position-turtle.pos())) == 0:
                self.is_game_on = False
