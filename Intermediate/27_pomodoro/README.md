# Pomodoro Timer

A GUI-based Pomodoro Timer application built in Python using `Tkinter`. The app uses the Pomodoro Technique to help users with time management by breaking work into intervals separated by short and long breaks.

***

### Features
- Implements the Pomodoro Technique with configurable work, short break, and long break intervals.
- Visual countdown timer with dynamic updates every second.
- Start and Reset buttons to control the timer.
- Displays checkmarks for completed work intervals.
- Color-coded timer label to indicate work time, short breaks, and long breaks.
- Simple and clean UI with tomato icon representing the Pomodoro theme.

***

### Pomodoro Technique
A popular time management method based on breaking work into focused 25-minute intervals separated by short 5-minute breaks, and a longer break after several cycles.

Default durations in this app:
- Work: 25 minutes
- Short Break: 5 minutes
- Long Break: 20 minutes (after 4 work sessions)

***

### Requirements
- Python 3.x  
- Tkinter (usually comes pre-installed with Python)
- An image file named `tomato.png` located in the same folder as the Python script for the tomato icon.

***

### How to Run
1. Download the source code and ensure `tomato.png` is present.  
2. Run the script using Python:

    ```bash
    python main.py
    ```

3. Use the **Start** button to begin the timer. The timer will cycle through work and break sessions automatically.  
4. Use the **Reset** button to stop the timer and reset sessions.

***

### Code Overview
- **Timer Mechanism**: The `start_timer()` function manages interval switching using repetition count.  
- **Countdown**: The `count_down()` function updates the timer display every second and triggers the next session when one finishes.  
- **Reset**: The `reset_timer()` function stops the timer and resets all counters and UI elements.  
- **UI Setup**: Tkinter widgets arranged in a grid with labels, canvas for the tomato image, and buttons.

***


### References
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)  
- [Pomodoro Technique Overview](https://en.wikipedia.org/wiki/Pomodoro_Technique)  

