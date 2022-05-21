import os
import time

def my_input(text, restrictions=[]):
    filtered = False
    input_res = ''
    while not filtered:
        input_res = input(text).strip()
        input_res_lower = input_res.lower()
        if input_res_lower == '':
            print("\nYou didn't enter any text.\n")
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


def pause(sec=1):
    time.sleep(sec)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
