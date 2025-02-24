# TODO: import random module
from random import randint
from art import logo1, logo2
from list import data_of_celebs
print(logo1)


# TODO: selecting another random celebrities from list random_celebrities which is not as given argument
def random_celeb(n):
    x = randint(0, 49)
    while x == n:
        x = randint(0, 49)
    return x


# TODO making a function that checks user's option is correct or not based on followers on INSTAGRAM.
def compare_followers(pos1, pos2):
    if data_of_celebs[pos1]['Followers'] > data_of_celebs[pos2]['Followers']:
        return True
    else:
        return False


def higher_lower():
    n1 = randint(0, 49)
    n2 = random_celeb(n=n1)
    score = 0
    while 5 > 4:
        print(f"Compare A: {data_of_celebs[n1]['Name']}, a {data_of_celebs[n1]['Profession']} from {data_of_celebs[n1]['Country']}.")
        print(logo2)
        print(f"Against B: {data_of_celebs[n2]['Name']}, a {data_of_celebs[n2]['Profession']} from {data_of_celebs[n2]['Country']}.")
        user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_answer == 'a' and compare_followers(pos1=n1, pos2=n2):
            score += 1
            print('you\'re right! and your current score ', score)
            n1 = n2
            n2 = random_celeb(n=n1)
        elif user_answer == 'b' and compare_followers(pos1=n2, pos2=n1):
            score += 1
            print('you\'re right! and your current score ', score)
            n1 = n2
            n2 = random_celeb(n=n1)
        elif (user_answer == 'a' and not compare_followers(pos1=n1, pos2=n2)) or (user_answer == 'b' and not compare_followers(pos1=n2, pos2=n1)):
            print('you are wrong and your score ', score)
            break


higher_lower()

