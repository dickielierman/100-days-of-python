import os
import random
from machine_data import MENU


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# TODO Custom input filtering to force our selections results.
def my_input(text, restrictions=[], datatype="str", hidden_restrictions=[]):
    if restrictions is None:
        restrictions = []
    filtered = False
    input_res = ''
    while not filtered:
        input_res = input(text).strip()
        input_res_lower = input_res.lower()
        if input_res_lower == '':
            print("\nYou didn't enter any text.\n")
        if datatype in ['float', 'int']:
            if not input_res_lower.isnumeric() and not isfloat(input_res_lower):
                print(f'\nInput must be a number.\n')
            elif len(restrictions) > 0 or len(hidden_restrictions) > 0:
                new_restrictions = restrictions + hidden_restrictions
                if input_res_lower not in new_restrictions:
                    print(f'\nAnswers are restricted to the following: {restrictions}.\n')
                else:
                    filtered = True
                    break
            else:
                filtered = True
                break

        elif len(restrictions) > 0 or len(hidden_restrictions) > 0:
            new_restrictions = restrictions + hidden_restrictions
            if input_res_lower not in new_restrictions:

                print(f'\nAnswers are restricted to the following: {restrictions}.\n')
            else:
                filtered = True
                break
        else:
            filtered = True
            break
    return input_res


# TODO: Print Resources Report
def print_resource_report():
    """When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
"""
    print()
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: {"${:,.2f}".format(resources["money"])}')
    print()


# TODO: Check resources sufficient?
def resource_check(selection, resources):
    """a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”
c. The same should happen if another resource is depleted, e.g. milk or coffee."""
    if not resources["water"] >= MENU[selection]["ingredients"]["water"]:
        print("Sorry, not enough water to complete this order.")
        return False
    elif ("milk" in MENU[selection]["ingredients"]) and not resources["milk"] >= MENU[selection]["ingredients"]["milk"]:
        print("Sorry, not enough milk to complete this order.")
        return False
    elif not resources["coffee"] >= MENU[selection]["ingredients"]["coffee"]:
        print("Sorry, not enough coffee to complete this order.")
        return False
    else:
        return True


# TODO: Process coins.
def process_coins(cost):
    """a. If there are sufficient resources to make the drink selected, then the program should
    prompt the user to insert coins.
    b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
    pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52"""
    paid = False
    total_entered = 0
    while not paid:
        print("Please insert coins.")
        quarters = int(my_input('How many quarters?', [], 'int'))
        dimes = int(my_input('How many dimes?', [], 'int'))
        nickles = int(my_input('How many nickles?', [], 'int'))
        pennies = int(my_input('How many pennies?', [], 'int'))
        total_entered = total_entered + (.25 * quarters) + (.10 * dimes) + (.05 * nickles) + (.01 * pennies)
        if total_entered < cost:
            needed_to_complete = cost - total_entered
            print(f"You've inserted {'${:,.2f}'.format(total_entered)}. You need to insert {'${:,.2f}'.format(needed_to_complete)} to complete your order.")
            continue_order = my_input("Would you like to continue 'c' or quit 'q'? ", ['c', 'q'])
            if continue_order == 'q':
                print(f"Cancelling transaction. Here's your {'${:,.2f}'.format(total_entered)} return")
                paid = False
                return {"quit": True, "return_amt": total_entered}
        else:
            change_amt = total_entered - cost
            paid = True
            return {"quit": False, "change_amt": change_amt}


# TODO: Make Coffee.
def make_coffee(drink, till, change):
    """a. If the transaction is successful and there are enough resources to make the drink the
    user selected, then the ingredients to make the drink should be deducted from the
    coffee machine resources.
    b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
    latte was their choice of drink."""
    change_text = ''
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    if "milk" in MENU[drink]["ingredients"]:
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    resources["money"] += till
    if change not in [0, 0.0]:
        change_text = f", and your change: {'${:,.2f}'.format(change)}"
    print(f"Here is your {drink}{change_text}. Enjoy!")


# TODO Custom functions to refill machine, and take out the money, not included in original project.
def refill_resources():
    """Updates resources dict with new values"""
    water = int(my_input('How many ml of water?', [], 'int'))
    milk = int(my_input('How many ml of milk?', [], 'int'))
    coffee = int(my_input('How many grams of coffee?', [], 'int'))
    resources["water"] += water
    resources["milk"] += milk
    resources["coffee"] += coffee


def get_paid():
    print(f"You've made {'${:,.2f}'.format(resources['money'])} today!")
    resources["money"] = 0


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
# TODO: Turn off the machine: end execution
# For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.
machine_power = True
print("Power on")
while machine_power:
    # TODO: Ask what drink? (espresso/latte/cappuccino)
    # a. Check the user’s input to decide what to do next.
    # b. The prompt should show every time action has completed, e.g. once the drink is
    # dispensed. The prompt should show again to serve the next customer.
    user_selection = my_input(f'What would you like? (espresso {"${:,.2f}".format(MENU["espresso"]["cost"])}/latte {"${:,.2f}".format(MENU["latte"]["cost"])}/cappuccino {"${:,.2f}".format(MENU["cappuccino"]["cost"])}): ', ['espresso', 'e', 'latte', 'l', 'cappuccino', 'c'], 'str', ['report', 'r', 'off', 'o', 'refill', '$'])
    if user_selection in ['off', 'o']:
        clear()
        machine_power = False
        break
    elif user_selection in ['report', 'r']:
        print_resource_report()
    elif user_selection in ['refill']:
        refill_resources()
    elif user_selection in ['$']:
        get_paid()
    else:
        if user_selection in ['espresso', 'e']:
            user_selection = 'espresso'
        elif user_selection in ['latte', 'l']:
            user_selection = 'latte'
        elif user_selection in ['cappuccino', 'c']:
            user_selection = 'cappuccino'
        if resource_check(user_selection, resources):
            # TODO: Check transaction successful?
            # a. Check that the user has inserted enough money to purchase the drink they selected.
            # E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
            # program should say “Sorry that's not enough money. Money refunded.”.
            # Modified to ask if the user would like to continue entering coins or quit. if continue, keep entering and checking amt. else quit and refund
            # b. But if the user has inserted enough money, then the cost of the drink gets added to the
            # c. If the user has inserted too much money, the machine should offer change.
            # E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
            # places.
            paid = process_coins(MENU[user_selection]["cost"])
            if not paid['quit']:
                make_coffee(user_selection, MENU[user_selection]["cost"], paid['change_amt'])
