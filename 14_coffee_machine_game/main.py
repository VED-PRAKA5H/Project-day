# TODO 1: import menu and resources
from list import MENU, resources
money = 0


# TODO 2: checks if resources are available or not
def remaining_resources(coffee_name):
    """this function calculate remaining resources of coffee and then take order if coffee were available"""
    taking_order = False
    for items in resources:
        if resources[items]-MENU[coffee_name]["ingredients"][items] < 0:
            print(f"Sorry there is not enough {items}.")
            break
        else:
            taking_order = True
    if taking_order:
        make_coffee(coffee_name=coffee_name)


# TODO 3: create a function that take coffee and takes coins and calculate it
def make_coffee(coffee_name):
    """serves coffee if given money is greater or equal to the particular coffee cost."""
    # where, quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    given_money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if given_money > MENU[coffee_name]['cost']:
        print(f"Here is ${round(given_money-MENU[coffee_name]['cost'],2)} in change.")
        print(f'Here is your {coffee_name} ☕️. Enjoy!')
        global money
        money += MENU[coffee_name]["cost"]
        for items in resources:
            resources[items] -= MENU[coffee_name]["ingredients"][items]
    else:
        print("Sorry that's not enough money. Money refunded.")


def report(item_name):
    """checks remaining resources before an order of a coffee"""
    if item_name == 'report':
        for items in resources:
            if items != "coffee":
                print(f"{items} : {resources[items]}ml")
            elif items == "coffee":
                print(f"{items} : {resources[items]}gm")
        print("money: $", money)
    else:
        remaining_resources(coffee_name=item_name)


def coffee():
    coffee_machine_on = True
    while coffee_machine_on:
        print("Turn off the coffee machine by entering 'off'. to see resources enter 'report'")
        user_answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_answer == 'off':
            coffee_machine_on = False
        else:
            report(item_name=user_answer)


coffee()
