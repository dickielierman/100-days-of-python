import art
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def my_input(text, restrictions=[], type="str"):
    filtered = False
    input_res = ''
    while not filtered:
        input_res = input(text).strip()
        input_res_lower = input_res.lower()
        if input_res_lower == '':
            print("\nYou didn't enter any text.\n")
        if type in ['float','int']:
            if not input_res_lower.isnumeric() and not isfloat(input_res_lower):
                print(f'\nInput must be a number.\n')
            else:
                filtered = True
                break
        elif len(restrictions) > 0:
            if input_res_lower not in restrictions:
                print(f'\nAnswers are restricted to the following: {restrictions}.\n')
            else:
                filtered = True
                break
        else:
            filtered = True
            break
    return input_res


def print_new_calc(new):
    number_of_spaces = 17
    blank_space = ''
    for i in range(number_of_spaces - len(new)):
        blank_space += ' '
    new_calc_text = '|' + blank_space + new + '|'
    clear()
    print(art.logo.replace('|Python Calculator|', '|                 |').replace('|  Dickie Lierman |', new_calc_text))
    return new_calc_text
def calculator():
    print(art.logo)
    num1 = float(my_input("What's the first number? ", [], 'float'))
    still_working = True
    while still_working:
        print_new_calc(str(num1))
        restrictions_list = []
        for operator in operations:
            restrictions_list.append(operator)
            print(f'{operator} = {operations[operator].__name__}')
        op = my_input("What operator would you like to use? ", restrictions_list)
        print_new_calc(f'{num1} {op}' )

        num2 = float(my_input("What's the second number? ", [], 'float'))
        print_new_calc(f'{num1} {op} {num2}')
        calc_function = operations[op]
        result = calc_function(num1, num2)
        print_new_calc(f'{num1} {op} {num2} = {result}')
        print(f'{num1} {op} {num2} = {result}')
        num1 = result
        print()
        lets_continue = my_input(f"Would you like you continue using {num1}? y or n: ", ['y', 'yes', 'n', 'no'])
        if lets_continue in ['no', 'n']:
            still_working = False
            clear()
            calculator()
            break
calculator()