import time
from turtle import Screen
from paddle import Paddle
from ball import Dot
from score_board import Score

dot_obj = Dot()
screen_obj = Screen()
screen_obj.tracer(0)

"""creating screen"""
screen_obj.bgcolor('black')
screen_obj.setup(800, 600)
screen_obj.title('Pong')

game_is_on = True
screen_obj.listen()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

screen_obj.onkey(r_paddle.down, 'Up')
screen_obj.onkey(r_paddle.up, 'Down')
screen_obj.onkey(l_paddle.down, "w")
screen_obj.onkey(l_paddle.up, "s")

l_score = Score(-100, 240)
r_score = Score(100, 240)
x = 0.1
while game_is_on:
    time.sleep(x)
    screen_obj.update()
    dot_obj.move_forward()

    if (abs(dot_obj.xcor()-l_paddle.xcor()) <= 20 and abs(dot_obj.ycor()-l_paddle.ycor()) < 50
            and dot_obj.heading() == 180):
        dot_obj.x_bounce()
        dot_obj.setheading(0)
        x *= 0.9

    elif (abs(dot_obj.xcor()-r_paddle.xcor()) <= 20 and abs(dot_obj.ycor()-r_paddle.ycor()) < 50
          and dot_obj.heading() == 0):
        dot_obj.x_bounce()
        dot_obj.setheading(180)
        x *= 0.9

    if dot_obj.ycor() > 280 or dot_obj.ycor() < -280:
        dot_obj.y_bounce()

    if dot_obj.xcor() > 380:
        x = 0.1
        l_score.score_l()
        dot_obj.home()
        dot_obj.x_bounce()
        dot_obj.setheading(180)

    elif dot_obj.xcor() < -380:
        x = 0.1
        dot_obj.home()
        dot_obj.x_bounce()
        r_score.score_r()
        dot_obj.setheading(0)


screen_obj.exitonclick()
