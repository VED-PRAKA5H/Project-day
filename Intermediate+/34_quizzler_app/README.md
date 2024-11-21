# Quizzler App

A graphical quiz application built with Python's Tkinter, leveraging the [Open Trivia Database API](https://opentdb.com/api_config.php) for quiz questions. This app provides an interactive way to learn by answering multiple-choice questions fetched dynamically from the web.

***

### Features
- Fetches trivia questions dynamically using the Open Trivia DB API.  
- Decodes HTML entities in questions and answers for proper display.  
- Clean and responsive GUI built with Tkinter.  
- Displays questions with multiple choices and handles user input.  
- Tracks and displays the score as the quiz progresses.  
- Supports different categories and question types depending on API usage (expandable).

***

### Requirements
- Python 3.x  
- `requests` package:

```bash
pip install requests
```

- Uses Python standard libraries `html` for unescaping HTML entities and `tkinter` for GUI.

***

### Setup

1. Clone or download the project files.  
2. If fetching questions from the API, ensure internet connectivity. Otherwise, use the bundled local `question_data` for offline mode.  
3. Make sure the dependencies are installed.

***

### How to Run

Run the main script:

```bash
python main.py
```

- The GUI window will open with questions and answer options.  
- Select your answer and proceed through the quiz.  
- Your score will update after each question.

***

### Code Overview

- `question_data`: Contains questions and answers (can be replaced with API call results).  
- `Question` class: Models a single question object.  
- `QuizBrain` class: Handles quiz logic, such as question progression and checking answers.  
- `QuizInterface` class: Builds the Tkinter GUI, displays questions, and handles user interactions.  
- Uses `html.unescape` to convert HTML entities like `&quot;` and `&amp;` to normal characters.

***


### References
- [Open Trivia DB API Documentation](https://opentdb.com/api_config.php)  
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)  
- [html.unescape() Python docs](https://docs.python.org/3/library/html.html#html.unescape)  
