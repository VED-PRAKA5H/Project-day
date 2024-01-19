import turtle
from turtle import Turtle, Screen
import colorgram
my_object = Turtle()
my_screen = Screen()
turtle.colormode(255)     # this colormode method activate RGB colormode
my_object.penup()
my_object.setposition(-200, -150)
my_object.pendown()
colors = colorgram.extract("image.jpg", 30)     #this extract method takes image name and no. of colors you want extract (provided it has that much colors in that image)
def right():
    my_object.penup()
    my_object.right(90)
    my_object.forward(40)
    my_object.right(90)
    my_object.forward(40)
    my_object.pendown()
def left():
    my_object.penup()
    my_object.left(90)
    my_object.forward(40)
    my_object.left(90)
    my_object.forward(40)
    my_object.pendown()

for i in range(100):
    first_color = colors[i%len(colors)]
    rgb = first_color.rgb
    red = rgb.r
    green = rgb.g
    blue = rgb.b
    my_object.dot(20, (red,green,blue))
    my_object.penup()
    my_object.forward(40)
    my_object.pendown()
    if my_object.xcor() == 200 and my_object.heading() == 0:
        left()
    if my_object.xcor() == -240 and my_object.heading() == 180:
        right()


