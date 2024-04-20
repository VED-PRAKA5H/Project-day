# Snake Game

A classic Snake game implemented in Python using the turtle graphics module. Control the snake with arrow keys, eat food to grow longer, and avoid running into the walls or yourself!

***

### Features
- Classic snake gameplay with smooth controls using arrow keys.  
- Randomly spawned food items to increase the snake’s length.  
- Collision detection with walls and the snake’s own tail to end the game.  
- Dynamic scoring system showing your current length/score.  
- Modular design with classes handling snake behavior, food, scoring, and growth logic.

***

### Project Structure

```text
project/
│
├── snake.py            # Snake class handling movement and control
├── food.py             # Food class for generating food at random positions
├── increase_length.py  # Manage snake growth and collision detection with tail
├── score_board.py      # Handles scoring display and game over message
├── main.py             # Entry point that runs the game loop and user input
├── score.txt           # Save New highest score
└── README.md           # This documentation file
```

***

### Installation & Setup

1. Clone the repository.

2. Install dependencies (if any; turtle usually comes pre-installed with Python):  
   ```bash
   pip install turtle
   ```

3. Run the game:  
   ```bash
   python main.py
   ```

***

### How to Play

- Use the arrow keys (Up, Down, Left, Right) to control the snake’s direction.  
- Eat the randomly placed food to grow longer and increase your score.  
- Avoid running into the edges of the game window or your own tail — either ends the game.  
- The game ends with a game over message showing your final score.

***

### Useful Links & References

- Python Turtle Graphics Documentation:  
  [Python Turtle Docs](https://docs.python.org/3/library/turtle.html)  
- Learn more about classic snake game mechanics and implementations online for inspiration.
