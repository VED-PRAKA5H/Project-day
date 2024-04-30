# Hindi to English Flash Card App

A flash card learning app built with Python's Tkinter GUI and Pandas to help users learn Hindi to English vocabulary interactively.

***

### Features
- Shows Hindi words on flash cards with a timer.
- Automatically flips the card after a count-down to reveal the English translation.
- Buttons to mark words as "Known" (right) or "Unknown" (wrong).
- Known words get removed from the learning list and saved for later progress tracking.
- Stores progress in a CSV file to resume learning where left off.
- Simple, clean, and user-friendly interface with images and color-coded elements.

***

### Requirements
- Python 3.x  
- Tkinter (usually pre-installed)  
- Pandas library for CSV file handling:

    ```bash
    pip install pandas
    ```

- Image files required in an `images` folder relative to the script:
  - `card_front.png`
  - `card_back.png`
  - `right.png`
  - `wrong.png`

- CSV data files in a `data` folder:
  - `hi_en_words.csv` (Hindi-English word list)
  - `to_learn.csv` (app-generated progress tracking file)

***

### How to Run
1. Ensure the required CSV and image files are in the correct folders (`data/` and `images/`).  
2. Run the script:

    ```bash
    python main.py
    ```

3. The app will show a Hindi word with a 5 second timer. After the timer, the card flips to the English translation.  
4. Mark words as "Known" by clicking the right button or "Unknown" by clicking the wrong button. Known words are removed from the learning list.  
5. Continue learning until all words are mastered.

***

### Code Overview
- **Data Loading**: Reads the full Hindi-English word list and tracks learning progress via saved CSV.  
- **Word Selection**: Randomly picks a Hindi word each cycle.  
- **Timer & Flip**: Counts down 5 seconds displaying Hindi word, then flips card to show English.  
- **User Interaction**: Buttons to mark correct or incorrect recall; updates progress accordingly.  
- **UI**: Tkinter-based canvas and buttons with thematic images and colors.

***


### References
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)  
- [Pandas Documentation](https://pandas.pydata.org/docs/)  
