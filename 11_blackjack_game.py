cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def win_status(user_cards, bot_cards):
    """This function tells about who is winner when sum first two cards is not 21."""
    while sum(bot_cards) < 17:
        card_value_for_bot = random.choice(cards)
        if sum(bot_cards) + card_value_for_bot > 21 and card_value_for_bot == 11:
            card_value_for_bot = 1
        bot_cards.append(card_value_for_bot)
    if sum(user_cards) > 21:
        print(f"your cards: {user_cards} and your score {sum(user_cards)}.\ncomputer's cards is: {bot_cards} and computer score {sum(bot_cards)}")
        print("YOU LOST.")
    elif sum(bot_cards) > 21:
        print(f"your cards: {user_cards} and your score {sum(user_cards)}.\ncomputer's cards is: {bot_cards} and computer score {sum(bot_cards)}")
        print("YOU WIN.")
    elif sum(user_cards) > sum(bot_cards):
        print(f"your cards: {user_cards} and your score {sum(user_cards)}.\ncomputer's cards is: {bot_cards} and computer score {sum(bot_cards)}")
        print('YOU WIN.')
    elif sum(user_cards) == sum(bot_cards):
        print(f"your cards: {user_cards} and your score {sum(user_cards)}.\ncomputer's cards is: {bot_cards} and computer score {sum(bot_cards)}")
        print('GAME DRAW.')
    elif sum(user_cards) < sum(bot_cards):
        print(f"your cards: {user_cards} and your score {sum(user_cards)}.\ncomputer's cards is: {bot_cards} and computer score {sum(bot_cards)}")
        print('YOU LOST.')
    return False


def first_two_cards():
    """This function adds first two cards and also tells about if the sum of first two cards is 21."""
    user = []
    bot = []
    continue_game = True
    for i in range(2):
        card_value_for_user = random.choice(cards)
        card_value_for_bot = random.choice(cards)
        if sum(user) + card_value_for_user > 21 and card_value_for_user == 11:
            card_value_for_user = 1
        user.append(card_value_for_user)
        if sum(bot) + card_value_for_bot > 21 and card_value_for_bot == 11:
            card_value_for_bot = 1
        bot.append(card_value_for_bot)
    if sum(bot) == 21:
        print('YOU LOST.')
        continue_game = False
    elif sum(user) == 21 and sum(bot) != 21:
        print('YOU ARE BLACKJACK.')
        continue_game = False
    return user, bot, continue_game,


def black_jack():
    user_bot_continue_game = list(first_two_cards())                  # return of first_two_cards() is tuple type so we converted it into list
    user = user_bot_continue_game[0]
    bot = user_bot_continue_game[1]
    continue_game = user_bot_continue_game[2]
    print('Your cards: ', user, 'Your current score: ', sum(user))
    print(f"computer first card is: {bot[0]}")
    add_card = 'y'
    while add_card == 'y' and continue_game:
        add_card = input("Type 'y' to get another card or Type 'n' to pass: ").lower()
        if add_card == 'y':
            card_value = random.choice(cards)
            if sum(user) + card_value > 21 and card_value == 11:
                card_value = 1
            user.append(card_value)
            if sum(user) > 20:
                win_status(user_cards=user, bot_cards=bot)
                continue_game = False
            else:
                print(f"your cards: {user} and your current score: {sum(user)}, computer's first card is: {bot[0]}")
    if add_card == 'n' and continue_game:
        win_status(user_cards=user, bot_cards=bot)


want_to_play = True
while want_to_play:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'n':
        want_to_play = False
    else:
        black_jack()

  
