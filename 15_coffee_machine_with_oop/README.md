# Coffee Machine Game (OOP Version)

An object-oriented simulation of a coffee vending machine. This project models the coffee machine functionality using Python classes to manage menu items, resource management, and payment processing.

## Overview

This version of the coffee machine game uses OOP principles to separate concerns into different classes:

- **Menu & MenuItem**: Handles available drink options and their details.
- **CoffeeMaker**: Manages coffee resources, checks availability, and prepares drinks.
- **MoneyMachine**: Handles all monetary transactions including payments and reporting.

The program prompts the user to choose a coffee, manages resources, receives payment, and delivers the drink while providing options to view reports or shut down the machine.

## How to Use

1. Run the main script.
2. Enter your coffee choice from the menu displayed.
3. Type `report` to see current resource availability and money earned.
4. Type `off` to turn off the machine.

Example interaction:

```
What would you like? espresso/latte/cappuccino: latte
Please insert coins.
how many quarters?: 10
how many dimes?: 0
how many nickles?: 0
how many pennies?: 0
Here is $0.5 in change.
Here is your latte ☕️. Enjoy!

What would you like? espresso/latte/cappuccino: report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

What would you like? espresso/latte/cappuccino: off
```

## Code Structure and Classes

- **Menu**: Contains a list of `MenuItem` objects. Provides methods to display items and find drinks by name.
- **MenuItem**: Represents a single coffee option with attributes for name, ingredients, and cost.
- **CoffeeMaker**:
  - Tracks available resources (water, milk, coffee).
  - Checks if resources are sufficient for the requested drink.
  - Updates resources after a drink is made.
  - Displays current resource report.
- **MoneyMachine**:
  - Handles coin input and calculates total payment.
  - Checks if inserted money covers the cost.
  - Processes transactions and keeps track of total money earned.
  - Reports total money collected.

## Features

- Modular design improves code organization and maintainability.
- Clear separation of concerns with dedicated classes.
- Interactive user interface with continuous prompts until shutdown.
- Accurate resource management and monetary transactions.

## Requirements

- Python 3.x
- The following project files (assumed to be in the same directory or package):
  - `menu.py` (with `Menu` and `MenuItem` classes)
  - `coffee_maker.py` (with `CoffeeMaker` class)
  - `money_machine.py` (with `MoneyMachine` class)
