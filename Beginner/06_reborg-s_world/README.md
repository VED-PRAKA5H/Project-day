# Reeborg's World - Solutions  

Reeborg's World is a programming environment designed to teach programming concepts by controlling a robot through mazes and hurdles. This repository contains Python solutions for two challenges: Maze navigation and Hurdle-4 obstacle course.  

### Maze Solution  
- The robot uses a "right-hand rule" method to navigate the maze.  
- It first orients to not face north, then continuously checks if it has reached the goal.  
- It turns right whenever possible and moves forward when the front is clear, avoiding walls and dead ends.  

### Hurdle-4 Solution  
- The robot detects obstacles (hurdles) in front and decides turns accordingly.  
- It tries to move right around hurdles when possible.  
- It handles complex hurdle sequences by turning left or right and moving forward carefully.  

### How to Run  
- Use the [Reeborg's World online platform](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json).  
- Copy and paste the Python code solutions into the code editor for the respective worlds.  
- Run and observe the robot solve the challenge.  

### Example Code Snippet for Maze  
```python
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
```
