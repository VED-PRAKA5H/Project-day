# Turtle Crossing Game 🐢🚗  

Help a turtle cross the road safely while avoiding cars! Each time the turtle makes it to the top, the level increases, and the game gets faster.  

***

### Features
- **Turtle Player**: Use arrow keys to move the turtle forward and backward.  
- **Cars**: Randomly generated cars that move left across the screen.  
- **Scoreboard**: Tracks the player’s level and displays a Game Over message when the turtle is hit.  
- **Increasing Difficulty**: With each successful level, the car speed increases.  

***

### Project Structure
```
project/
│── main.py             # Entry point of the game
│── turtle_player.py    # Player logic (turtle movement, level-up)
│── cars.py             # Car class and movement
│── scoreboard.py       # Score and game over logic
│── README.md           # Project documentation
```

***

### How to Play
1. Run `main.py`.  
2. Use the **Up Arrow (↑)** to move the turtle forward and the **Down Arrow (↓)** to move it backward.  
3. Reach the top of the screen to level up.  
4. Avoid collisions with cars.  
5. Survive as long as possible while the game speed increases.  

***

### Requirements
- Python 3.7+  
- `turtle` (comes pre-installed with Python)  
- No external dependencies  

***
