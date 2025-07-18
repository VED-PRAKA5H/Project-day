import pandas
# Load the data
df = pandas.read_csv("nato_phonetic_alphabet.csv")
# TODO 1: create a dictionary in format {column1_data1: column2_data1, ...}

nato_alphabet_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# TODO 2: take input from user then create a list
while True:
    user_word = list(input("Enter a word to find NATO phonetic: ").upper())
    try:
        answer_list = [nato_alphabet_dict[letter] for letter in user_word]
        print(answer_list)
        break
    except KeyError:
        print("Sorry only letter in the alphabet please.")
