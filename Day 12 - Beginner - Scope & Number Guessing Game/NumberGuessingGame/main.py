# Number Guessing Game Objectives:
from art import logo
import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def my_input(text, restrictions=[], type="str"):
    if restrictions is None:
        restrictions = []
    filtered = False
    input_res = ''
    while not filtered:
        input_res = input(text).strip()
        input_res_lower = input_res.lower()
        if input_res_lower == '':
            print("\nYou didn't enter any text.\n")
        if type in ['float', 'int']:
            if not input_res_lower.isnumeric() and not isfloat(input_res_lower):
                print(f'\nInput must be a number.\n')
            else:
                if len(restrictions) > 0:
                    if int(input_res_lower) < restrictions[0] or int(input_res_lower) > restrictions[1]:
                        print(f'\nAnswer should be between {restrictions[0]} & {restrictions[1]}.\n')
                    else:
                        filtered = True
                        break
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


def check_guess(guess, answer):
    if guess > answer:
        print("Too high")
        return False
    elif guess < answer:
        print("Too low")
        return False
    else:
        print(f"You win! {answer} was the secret number")
        return True


def the_game():
    answer = random.randint(1, 100)
    print(logo)
    winner = False
    guessed = []
    difficulty = my_input("Would you like 'hard' difficulty or 'easy'? ", ['hard', 'easy', 'h', 'e'])
    if difficulty in ['hard', 'h']:
        guesses = 5
    else:
        guesses = 10
    while guesses > 0 and not winner:
        guess = int(my_input(f"Please enter your guess ({guesses} remaining): ", [1, 100], 'int'))
        if guess in guessed:
            print(f"You've already guessed {guess}")
        else:
            guessed.append(guess)
            check = check_guess(guess, answer)
            if check:
                winner = check
            else:
                guesses -= 1
    if guesses == 0:
        print(f'Sorry, you ran out of guesses. The answer was {answer}')
    if my_input("Would you like to play again? y or n: ", ['y', 'n']) == 'y':
        clear()
        the_game()


the_game()
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
