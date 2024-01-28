from turtle import Turtle, Screen
import random, turtle
screen1 = Screen()
my_object1 = Turtle()
my_object2 = Turtle()
my_object3 = Turtle()
my_object4 = Turtle()
my_object5 = Turtle()
object_list = [my_object1, my_object2, my_object3, my_object4, my_object5]
for i in [1, 2, 3, 4, 5]:
    color = ['green', 'blue', 'red', 'yellow', 'black']
    object_list[i - 1].color(color[i - 1])
    object_list[i - 1].shape('turtle')
    object_list[i - 1].penup()
    object_list[i - 1].turtlesize(2)
    object_list[i - 1].setposition(-700, 300 - i * 100)

my_object = Turtle()
my_object.pensize(5)
my_object.hideturtle()
my_object.penup()
my_object.setposition(690, 400)
my_object.right(90)
my_object.pendown()
my_object.fd(800)
user = screen1.textinput('who will win?', "which turtle will win?")
turtle.listen(1,0)

while True:
    my_object1.forward(random.randint(5, 10))
    my_object2.forward(random.randint(5, 10))
    my_object3.forward(random.randint(5, 10))
    my_object4.forward(random.randint(5, 10))
    my_object5.forward(random.randint(5, 10))
    if my_object1.xcor() >= 690 or my_object2.xcor() >= 690 or my_object3.xcor() >= 690 or my_object4.xcor() >= 690 or my_object5.xcor() >= 690:
        break
dead_line = 690
color = my_object1.color()
for objects in [my_object1, my_object2, my_object3, my_object4, my_object5]:
    if objects.xcor() >= dead_line:
        dead_line = objects.xcor()
        color = objects.pencolor()
        if user.lower() == color:
            print('you win')
        else:
            print("you lose")
        winner = f"turtle of {color} color is the winner"
        screen1.textinput(winner, 'enter ok to exit')

screen1.exitonclick()

