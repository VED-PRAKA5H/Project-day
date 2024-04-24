import turtle

import pandas as pd
from score_board import Score
import time
from turtle import Turtle, Screen

# screen setup
screen = Screen()
screen.setup(700, 700)
screen.bgpic('bharat.gif')

# register a shape in turtle
# image = 'bharat.gif'
# screen.addshape(image)


# creating turtle object
turtle_obj = Turtle()
turtle_obj.penup()
turtle_obj.hideturtle()

# create dataframe by reading CSV file using pandas
df = pd.read_csv('36_states_UTs.csv')
x_cor_of_states = df.X
y_cor_of_states = df.Y
states_and_uts = df.States_and_Uts

# create score on screen
score = Score()


def create_dot():
    """this will make dot on the particular location when called"""
    turtle_obj.pendown()
    turtle_obj.dot()
    turtle_obj.penup()


def show_states_name(i):
    """this will write states and UTs name in their locations"""
    if states_and_uts[i] == 'Dadra and Nagar Haveli and Daman and Diu'.title():
        """this location has multiple places that is x and y coord are in string that contains a list
            first we remove square bracket by strip method and then we make this string into list using
             split method separated by ',' """
        x = x_cor_of_states[i].strip('[]').split(',')
        y = y_cor_of_states[i].strip('[]').split(',')
        turtle_obj.goto(float(x[0]), float(y[0]))
        turtle_obj.write('Dadra and Nagar Haveli and Daman')
        turtle_obj.forward(168)
        create_dot()
        turtle_obj.goto(float(x[1]), float(y[1]))
        turtle_obj.write('Diu')
        create_dot()
    else:
        turtle_obj.goto(float(x_cor_of_states[i]), float(y_cor_of_states[i]))
        create_dot()
        turtle_obj.write(states_and_uts[i])


answered_states = []
tic = time.time()
game_is_on = True
while len(answered_states) < 36:
    answer = screen.textinput('Guess the State or UT name', 'what is another name?').title()

    states_uts_list = states_and_uts.to_list()

    if answer in states_uts_list and answer not in answered_states:
        position_of_states = states_uts_list.index(answer)
        show_states_name(position_of_states)
        answered_states.append(answer)

    elif answer.lower() == 'exit':
        unanswered_names = [states for states in states_uts_list if states not in answered_states]
        unanswered_names_dict = {'unanswered_names': unanswered_names,
                                 }
        data = pd.DataFrame(unanswered_names_dict)
        data.to_csv('missing_states.csv')
        for _ in unanswered_names:
            show_states_name(states_uts_list.index(_))
        break

    if int((time.time()-tic)/60) == 5:
        print('time over ⌛')
        break
    score.show_score(len(answered_states), time.time() - tic)
turtle.mainloop()
