import random
import os
import time


def pause(sec=1):
    time.sleep(sec)


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


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


def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Return calculated score from cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw."
    elif computer_score == 0:
        return "You lose, opponent has a Blackjack."
    elif user_score == 0:
        return "You win with a Blackjack1"
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose."

def blackjack():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your hand: {user_cards} Current hand total: {user_score}")
        print(f"Computer hand [{computer_cards[0]}, ?] Current hand total: ?")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = my_input("Type 'y' to hit, or 'n' to pass: ", ['y', 'n'])
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                clear()
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand was {user_cards} totalling {sum(user_cards)}")
    print(f"Dealers final hand was {computer_cards} totalling {sum(computer_cards)}")
    print(compare(user_score, computer_score))
    while my_input("Do you want to play another hand? y or n: ", ['y', 'n']) == 'y':
        clear()
        blackjack()
blackjack()

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
