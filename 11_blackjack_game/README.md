# Blackjack Game

A simple console-based Blackjack (21) game where you play against the dealer (computer). This project demonstrates basic game logic, card handling, and user interaction using Python.

## Overview

Blackjack is a classic casino card game where the goal is to get card values as close to 21 as possible without going over. Players compete against the dealer by drawing cards and attempting to beat the dealer's hand.

This implementation includes:
- Random card drawing with appropriate Ace (11 or 1) handling.
- Dealer (bot) logic to draw until reaching a minimum score.
- Win/loss/draw conditions including natural Blackjack.
- User input to draw additional cards or pass.

## How to Play

1. Run the script.
2. You will be dealt two initial cards.
3. The dealer shows one card face up.
4. Choose whether to draw additional cards or pass.
5. The dealer draws cards automatically as per Blackjack rules.
6. The winner is decided based on the final card sums.

## Code Structure

- `cards`: List of card values (with face cards represented as 10 and Ace as 11).
- `first_two_cards()`: Deals the initial two cards to both user and dealer.
- `win_status(user_cards, bot_cards)`: Determines and prints the game result.
- `black_jack()`: Manages the game flow for user actions and dealer drawing.
- A loop to allow repeated games based on user input.

## Usage

Run the script and follow on-screen prompts to play multiple rounds:

```
python main.py
```

Example interaction:

```
Do you want to play a game of Blackjack? Type 'y' or 'n': y
Your cards:   Your current score:  15
computer first card is: 10
Type 'y' to get another card or Type 'n' to pass: y
...
```

## Features

- Ace cards count as 11 or 1 depending on the hand's total.
- Dealer hits until score is at least 17.
- Checks for natural Blackjack (21 from first two cards).
- Result messages for win, loss, or draw.

## References

For playing online Blackjack and rules understanding, see [Online Blackjack Game](https://games.washingtonpost.com/games/blackjack).

---

Enjoy playing and feel free to contribute!
