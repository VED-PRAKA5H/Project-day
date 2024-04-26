# NATO Alphabet Converter

**Convert any word into the NATO phonetic alphabet using Python and pandas.**

***

### Features

- **Data-Driven:** Uses a CSV file containing the NATO alphabet mapping (letters to code words).
- **User Input:** Takes a word from the user and converts each letter into its NATO phonetic equivalent.
- **Error Handling:** Alerts users if the input contains characters outside the standard alphabet.
- **Simple & Interactive:** Runs in the console with immediate feedback.

***

### Project Structure

```
NATO-Alphabet-Converter/
│── nato_phonetic_alphabet.csv     # CSV file mapping letters to NATO code words
│── main.py                        # Python script to run the conversion
│── README.md                     # This documentation file
```

***

### How It Works

- Loads the CSV file into a pandas DataFrame.
- Creates a dictionary mapping each letter to its NATO code word.
- Prompts the user to enter a word.
- Converts each letter of the input to the corresponding NATO word, validating input.
- Prints the phonetic representation as a list of code words.

***

### Requirements

- **Python 3.x**
- **pandas** (`pip install pandas`)

***

### Usage Instructions

1. Clone or download this repository.
2. Ensure `nato_phonetic_alphabet.csv` and the script are in the same folder.
3. Run the script in the terminal:
   ```
   python main.py
   ```
4. Enter a word when prompted to see its NATO phonetic alphabet conversion.
5. Input is case-insensitive but must consist of English letters only.

***

### Example

```
Enter a word to find NATO phonetic: hello
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```
