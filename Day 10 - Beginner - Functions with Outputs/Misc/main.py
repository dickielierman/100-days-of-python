import os
import time

# def my_input(text, restrictions=[]):
#     filtered = False
#     input_res = ''
#     while not filtered:
#         input_res = input(text).strip()
#         input_res_lower = input_res.lower()
#         if input_res_lower == '':
#             print("\nYou didn't enter any text.\n")
#         elif len(restrictions) > 0:
#             if input_res_lower not in restrictions:
#                 print(f'\nAnswers are restricted to the following: {restrictions}.\n')
#             else:
#                 filtered = True
#                 break
#         else:
#             filtered = True
#             break
#     return input_res


def pause(sec=1):
    time.sleep(sec)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def format_name(f_name, l_name):
    return f'{f_name.title().strip()} {l_name.title().strip()}'


print(format_name("rIcHaRd", "liERMan"))


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


print(add(2, multiply(5, divide(8, 4))))