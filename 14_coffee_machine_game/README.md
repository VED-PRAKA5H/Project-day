# Coffee Machine Game

A console-based simulation of a coffee machine that manages resources, processes coin input, and serves coffee based on user selection.

## Overview

This program simulates the operation of a coffee vending machine with limited resources (water, milk, coffee). Users can order different types of coffee: espresso, latte, or cappuccino. The machine checks if enough ingredients are available, processes coins input for payment, calculates change, and updates resources accordingly. Users can also request a report of remaining resources and total money earned or turn off the machine.

## How it Works

- The machine starts with predefined ingredient resources.
- The user is prompted to select their desired coffee or execute commands (`report`, `off`).
- The machine verifies if resources are sufficient to make the selected coffee.
- If enough resources are available, it asks the user to insert coins.
- It calculates the total money inserted and checks if it covers the cost of the coffee.
- If payment is sufficient, it serves the coffee, updates resources, and returns change if necessary.
- If payment is insufficient, the money is refunded.
- Users can view the remaining resources and total money earned by entering `report`.
- The machine can be turned off by entering `off`.

## Features

- Tracks and manages ingredient quantities (water, milk, coffee).
- Handles multiple coffee types with different ingredient requirements and prices.
- Processes coin input and calculates change.
- Reports current status of resources and total money collected.
- Graceful shutdown command to turn off the coffee machine.

## Code Structure

- `MENU` and `resources` imported from an external `list` module defining coffee recipes and available ingredients.
- `remaining_resources(coffee_name)`: Checks if there are enough resources to make the coffee.
- `make_coffee(coffee_name)`: Processes coin input, checks payment, serves coffee, and updates resources.
- `report(item_name)`: Either prints a resource/money report or triggers resource check and coffee preparation.
- `coffee()`: Main loop handling user input commands for ordering coffee, resource reporting, or turning off the machine.

## Usage

Run the Python script and follow prompts to order coffee or interact with the machine:

```
python main.py
```

Example session:

```
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
how many quarters?: 10
how many dimes?: 0
how many nickles?: 0
how many pennies?: 0
Here is $0.5 in change.
Here is your latte ☕️. Enjoy!
What would you like? (espresso/latte/cappuccino): report
water : 100ml
milk : 50ml
coffee : 50gm
money: $ 2.5
What would you like? (espresso/latte/cappuccino): off
```



