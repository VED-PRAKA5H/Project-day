# Quiz Game

A simple Python-based quiz game where you can test your knowledge by answering trivia questions. The questions and answers are dynamically fetched from the [Open Trivia Database](https://opentdb.com/).

***

## Features
- Fetches trivia questions from the Open Trivia DB API.  
- Keeps track of your progress and score.  
- Interactive command-line interface for answering questions.  
- Simple and beginner-friendly Python project.  

***

## Project Structure
```text
project/
│
├── data.py            # Fetches question data from API (OpenTriviaDB)
├── question_model.py  # Defines the Question class
├── quiz_brain.py      # Handles game logic
├── main.py            # Entry point for running the game
└── README.md          # Project documentation
```

***

## How It Works
1. `data.py` fetches JSON trivia questions and stores them in `question_data`.  
2. `main.py` converts each question and correct answer into a `Question` object.  
3. The `QuizBrain` class:
   - Presents questions to the user.  
   - Accepts input for answers.  
   - Tracks score and current question number.  
4. Once the quiz ends, your final score is displayed.  

***

## Example Run
```
Q.1: The sky is blue. (True/False): True
You got it right!
Your current score: 1/1

Q.2: The capital of France is Berlin. (True/False): False
You got it right!
Your current score: 2/2

You have completed the quiz.
Your final score was: 8/10
```

***

## Installation & Setup
1. Clone the repository:  

2. Install dependencies (if required):  
   ```bash
   pip install requests
   ```

3. Run the game:  
   ```bash
   python main.py
   ```
