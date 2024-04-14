def turn_right():
    turn_left()
    turn_left()
    turn_left()


while at_goal() is False:
    if front_is_clear() is not True:
        if right_is_clear() is True:
            turn_right()
            move()
        elif right_is_clear() is False:
            turn_left()
            if front_is_clear() is True:
                move()
            else:
                turn_left()
        else:
            turn_left()
            move()
    elif front_is_clear() is True:
        if right_is_clear() is True:
            turn_right()
            move()
        else:
            move()
