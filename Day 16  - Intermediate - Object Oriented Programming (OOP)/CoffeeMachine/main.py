from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mrs_coffee = CoffeeMaker()
till = MoneyMachine()
menu = Menu()
power_on = True
while power_on:
    skip = False
    selection = input(f"Please make a selection. ({menu.get_items()})").lower()
    if selection == 'report':
        print(mrs_coffee.report())
        print(till.report())
        skip = True
    elif selection in ['latte', 'l']:
        order_name = 'latte'
    elif selection in ['espresso', 'e']:
        order_name = 'espresso'
    elif selection in ['cappuccino', 'c']:
        order_name = 'cappuccino'
    elif selection == 'off':
        power_on = False
        break
    else:
        print("Command not recognized.")
        skip = True
    if not skip:
        drink = menu.find_drink(order_name)
        if mrs_coffee.is_resource_sufficient(drink):
            if till.make_payment(drink.cost):
                mrs_coffee.make_coffee(drink)

