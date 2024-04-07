def turn_right():
    turn_left()
    turn_left()
    turn_left()


while is_facing_north() is True:
    turn_left()
while at_goal() is False:
    if front_is_clear() is False:
        if right_is_clear() is True:
          turn_right()
          move()
        elif right_is_clear() is False:
           turn_left()    
    if right_is_clear() is True and front_is_clear() is True:
        turn_right()
        move()
    if front_is_clear() is True:
        move()        
