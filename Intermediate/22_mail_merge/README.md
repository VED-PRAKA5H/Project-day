# Mail Merge

Generate personalized letters automatically using a template and a list of names.

***

### Features

- **Bulk Personalization**: Automatically fills each recipient’s name into a template letter.
- **Automated Output**: Saves personalized letters as separate files in a designated output directory.
- **Template-Based**: Uses a customizable starting letter as the base for all outputs.
- **Input Flexibility**: Reads recipient names from a plain text file (one name per line).

***

### Project Structure

```
project/
│── main.py               # Script for generating letters
│── Input/
│   ├── Letters/
│   │   └── starting_letter.txt   # Letter template file
│   └── Names/
│       └── invited_names.txt     # List of recipient names
│── Output/
│   └── ReadyToSend/     # Directory for generated personalized letters
│── README.md            # Project documentation
```

***

### How It Works

- Place the letter template in the specified input folder.
- Place the list of names (one name per line) in the names file.
- Run the main script.
- The script will create an output directory (if needed) and generate a separate letter for each name, replacing the `[name]` placeholder with the actual name.

***

### Requirements

- Python 3.x
- No additional Python packages required (uses built-in modules only)

***

### Usage

1. Prepare your template letter with a `[name]` placeholder where the recipient’s name should go.
2. List all recipient names, one on each line, in the names input file.
3. Run the main script in your terminal or command prompt.
4. Personalized letters will be saved inside the output folder, ready to send.
