import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def win_status(user_cards, bot_cards):
    """This function tells about who is winner when sum first two cards is not 21."""
    while sum(bot_cards) < 17:
        card_value_for_bot = random.choice(cards)
        bot_cards.append(card_value_for_bot)
        if sum(bot_cards) > 21 and 11 in bot_cards:
            bot_cards.remove(11)
            bot_cards.append(1)
    if bot_cards[0]+bot_cards[1] == 21 and user_cards[0]+user_cards[1] != 21:
        print(f"your cards: {user_cards} and your score {sum(user_cards)}.\n"
              f"computer's cards is: {bot_cards} and computer score {sum(bot_cards)}")
        print('YOU LOST,Opponent has BLACKJACK.')
    elif user_cards[0]+user_cards[1] == 21 and bot_cards[0]+bot_cards[1] != 21:
        print(f"your cards: {user_cards} and your score {sum(user_cards)}.\n"
              f"computer's cards is: {bot_cards} and computer score {sum(bot_cards)}")
        print('YOU ARE BLACKJACK.')
    elif sum(user_cards) > 21:
        print(f"your cards: {user_cards} and your score {sum(user_cards)}.\n"
              f"computer's cards is: {bot_cards[:2]} and computer score {bot_cards[0]+bot_cards[1]}")
        print("YOU LOST.")
    elif sum(bot_cards) > 21:
        print(f"your cards: {user_cards} and your score {sum(user_cards)}.\n"
              f"computer's cards is: {bot_cards} and computer score {sum(bot_cards)}")
        print("YOU WIN.")
    elif sum(user_cards) > sum(bot_cards):
        print(f"your cards: {user_cards} and your score {sum(user_cards)}.\n"
              f"computer's cards is: {bot_cards} and computer score {sum(bot_cards)}")
        print('YOU WIN.')
    elif sum(user_cards) == sum(bot_cards):
        print(f"your cards: {user_cards} and your score {sum(user_cards)}.\n"
              f"computer's cards is: {bot_cards} and computer score {sum(bot_cards)}")
        print('GAME DRAW.')
    elif sum(user_cards) < sum(bot_cards):
        print(f"your cards: {user_cards} and your score {sum(user_cards)}.\n"
              f"computer's cards is: {bot_cards} and computer score {sum(bot_cards)}")
        print('YOU LOST.')


def first_two_cards():
    """This function adds first two cards and also tells about if the sum of first two cards is 21."""
    user = []
    bot = []
    for i in range(2):
        card_value_for_user = random.choice(cards)
        user.append(card_value_for_user)
        card_value_for_bot = random.choice(cards)
        bot.append(card_value_for_bot)
        if sum(user) > 21 and 11 in user:
            user.remove(11)
            user.append(1)
        if sum(bot) > 21 and 11 in bot:
            user.remove(11)
            user.append(1)
    return user, bot,


def black_jack():
    user_bot = list(first_two_cards())  # return of first_two_cards() is tuple type so we converted it into list
    user = user_bot[0]
    bot = user_bot[1]
    add_card = 'y'
    while add_card == 'y' and sum(user) != 21:
        print('Your cards: ', user, 'Your current score: ', sum(user))
        print(f"computer first card is: {bot[0]}")
        add_card = input("Type 'y' to get another card or Type 'n' to pass: ").lower()
        if add_card == 'y':
            card_value = random.choice(cards)
            user.append(card_value)
            if sum(user) > 21 and 11 in user:
                user.remove(11)
                user.append(1)
            if sum(user) > 20:
                win_status(user_cards=user, bot_cards=bot)
                break
    if add_card == 'n' or sum(user) == 21:
        win_status(user_cards=user, bot_cards=bot)


want_to_play = True
while want_to_play:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'n':
        want_to_play = False
    else:
        black_jack()

