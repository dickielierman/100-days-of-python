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


class Player:
    def __init__(self):
        self.inhand = []

    def deal_card(self):
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.inhand.append(random.choice(cards))

    def hand(self, secret=False):
        if secret:
            filler = '[' + str(self.inhand[0])
            tcount = len(self.inhand) - 1
            for i in range(tcount):
                filler += ', $'
            filler += ']'
            return filler
        return self.inhand

    def calculate_score(self, secret=False):
        """Return calculated score from cards"""
        if secret:
            return '?'
        if sum(self.inhand) == 21 and len(self.inhand) == 2:
            return 0
        if 11 in self.inhand and sum(self.inhand) > 21:
            self.inhand.remove(11)
            self.inhand.append(1)
        return sum(self.inhand)


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
    user = Player()
    dealer = Player()

    is_game_over = False

    for i in range(2):
        user.deal_card()
        dealer.deal_card()
    while not is_game_over:
        clear()
        user_score = user.calculate_score()
        computer_score = dealer.calculate_score()
        print(f"Your hand: {user.hand()} Current hand total: {user.calculate_score()}")
        print(f"Computer hand {dealer.hand(True)} Current hand total: {dealer.calculate_score(True)}")
        if user.calculate_score() == 0 or dealer.calculate_score() == 0 or user.calculate_score() > 21:
            is_game_over = True
        else:
            user_should_deal = my_input("Type 'y' to hit, or 'n' to pass: ", ['y', 'n'])
            if user_should_deal == 'y':
                user.deal_card()
            else:
                clear()
                is_game_over = True
    while dealer.calculate_score() != 0 and dealer.calculate_score() < 17:
        dealer.deal_card()
    clear()
    print(f"Your final hand was {user.hand()} totalling {sum(user.hand())}")
    print(f"Dealers final hand was {dealer.hand()} totalling {sum(dealer.hand())}")
    print(compare(user.calculate_score(), dealer.calculate_score()))
    while my_input("Do you want to play another hand? y or n: ", ['y', 'n']) == 'y':
        clear()
        blackjack()
blackjack()