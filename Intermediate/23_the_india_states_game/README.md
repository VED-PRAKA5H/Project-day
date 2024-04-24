# The India States Game

**Test your knowledge of Indian geography! Guess the locations of Indian states and union territories directly on the map.**

***

### Features

- **Geography Challenge:** Guess and identify all Indian states and union territories by name.
- **Interactive Map:** Each correct guess reveals and labels the state/UT on a map of India.
- **Data Integration:** Uses a CSV file with coordinates for each state and UT.
- **Scoreboard:** Tracks the number of correct answers and displays the score with elapsed time.
- **Save Progress:** Exiting the game saves a CSV of unguessed states for further practice.
- **Timed Play:** Option to play against the clock for an additional challenge.

***

### Project Structure

```
project/
│── main.py                  # Main game logic
│── score_board.py           # Score display logic
│── 36_states_UTs.csv        # Data file with state names and coordinates
│── bharat.gif               # India map image for background
│── missing_states.csv       # Auto-generated for unguessed states
│── README.md                # Project documentation
```

***

### How It Works

- The game window shows a map of India.
- On each turn, type the name of an Indian state or UT.
- Correct answers are marked and labeled at their actual map locations.
- An input of "exit" ends the game and exports a CSV with any names that weren't guessed.
- Game includes special handling for states with multiple geographical components.

***

### Requirements

- **Python 3.x**
- **pandas** (see [pandas documentation] for reference)
- **turtle** (standard module, for graphics)

***

### References

- Inspired by online map quizzes like [sporcle](https://www.sporcle.com/games/g/states).
- For detailed data handling and function usage, visit the [pandas documentation](https://pandas.pydata.org/docs/)
- Official pandas API Reference: https://pandas.pydata.org/docs/reference/index.html
