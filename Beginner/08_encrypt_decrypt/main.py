alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encode_decode_func(Text, Shift, Direction):
    sentence = Text.split()
    answer_sentence = []
    for word in sentence:
        answer = "encoded"
        answer_word = ""
        for letter in word:
            if letter in alphabet:
                position = alphabet.index(letter)
                if Direction == "encode":
                    position = (position + Shift) % 26
                elif Direction == "decode":
                    position = (position - Shift) % 26
                    answer = "decoded"
                answer_word += alphabet[position]
            elif letter not in alphabet:
                answer_word += letter
        answer_sentence.append(answer_word)
    print(f'the {answer} text of {Text} is: {" ".join(answer_sentence)}')


def ask_for_response():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift/key number:\n"))
    encode_decode_func(Text=text, Shift=shift, Direction=direction)
    print('Want to restart this program? Type yes or no.')
    ask = input().lower()
    if ask == 'yes':
        ask_for_response()
    else:
        print('goodbye')


ask_for_response()

# METHOD2👇

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
# 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
# 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#     shift_amount *= -1
#   for char in start_text:

#     if char in alphabet:
#       position = alphabet.index(char)
#       new_position = position + shift_amount
#       end_text += alphabet[new_position]
#     else:
#       end_text += char
#   print(f"Here's the {cipher_direction}d result: {end_text}")

# should_end = False
# while not should_end:

#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#   text = input("Type your message:\n").lower()
#   shift = int(input("Type the shift number:\n"))

#   shift = shift % 26

#   caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#   restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
#   if restart == "no":
#     should_end = True
#     print("Goodbye")
