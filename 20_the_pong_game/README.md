# The Pong Game

A classic Pong game implemented using Python’s turtle graphics module. This two-player game features paddles controlled by keyboard keys and a bouncing ball that increases speed over time.

***

### Features
- Classic Pong gameplay with two paddles controlled by different keys.  
- Ball movement with collision detection against paddles and screen edges.  
- Score tracking for both left and right players.  
- Gradually increases ball speed with each paddle hit to increase difficulty.  
- Structured build with 8 core development parts for modular design.

***

### Project Structure

```text
project/
│
├── paddle.py         # Paddle class to create and move paddles
├── ball.py           # Ball class managing the dot movement and bouncing logic
├── score_board.py    # Scoreboard class to track and display scores
├── main.py           # Main game loop with event handling and game logic
└── README.md         # Project documentation
```

***

### Installation & Setup

1. Clone the repository.

2. Install dependencies (if not already present):  
   ```bash
   pip install turtle
   ```

3. Run the game:  
   ```bash
   python main.py
   ```

***

### How to Play

- Player 1 (left paddle) controls:  
  - Move up: `w` key  
  - Move down: `s` key  

- Player 2 (right paddle) controls:  
  - Move up: Up Arrow key  
  - Move down: Down Arrow key  

- The ball bounces off paddles and top/bottom edges.  
- If the ball passes a paddle, the opponent scores a point.  
- The game continues with the ball resetting and speed adjusting for increasing challenge.

***

### Game Development Stages

1. Create the game screen with background and window size.  
2. Create and control the first paddle with keyboard inputs.  
3. Create the second paddle controlled by different keys.  
4. Create the ball (dot) and implement its forward movement.  
5. Detect collision with the top and bottom walls and bounce the ball.  
6. Detect collision with paddles and bounce the ball accordingly.  
7. Detect when a paddle misses the ball and award points.  
8. Keep and display the score for both players.

***

### Useful Links

- Python Turtle Graphics Documentation:  
  [Python Turtle Docs](https://docs.python.org/3/library/turtle.html)  
- General game logic inspiration from classic Pong implementations.
