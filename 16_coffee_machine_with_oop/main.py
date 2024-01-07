from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
continue_machine = True
while continue_machine:
    order_name = input(f"what would you like? {menu.get_items()}: ").lower()
    if order_name == "report":
        coffee_maker.report()
        money_machine.report()
    elif order_name == "off":
        continue_machine = False
    else:
        drink = menu.find_drink(order_name=order_name)
        if coffee_maker.is_resource_sufficient(drink=drink):
            drink_cost = drink.cost
            if money_machine.make_payment(cost=drink_cost):
                coffee_maker.make_coffee(order=drink)
