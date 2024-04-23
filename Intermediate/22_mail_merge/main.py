import os

directory = './Output/ReadyToSend'
if not os.path.exists(directory):
    os.makedirs(directory)

with open('Input/Letters/starting_letter.txt') as file:
    letter = file.read()
with open('Input/Names/invited_names.txt') as f:
    x = f.read()
    y = x.split('\n')
    for name in y:
        with open('Input/Letters/starting_letter.txt') as file:
            file_path = f'{directory}/letter_for_{name}.txt'
            new_letter = letter.replace('[name]', name)
            with open(file_path, "w") as file1:
                file1.write(new_letter)

# #################################### METHOD 2#########################################
#
# PLACEHOLDER = "[name]"
#
#
# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()
#
# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_letter)
