# clear the screen
#
# Import and display the logo
#
# if winning print: You're right! Current Score: {current score}
#
# create a get_random_card function to get random data that isn't equal to the data we just compared it to
# It will return 'name', 'follower_count', 'description', 'country'
#
# Compare A: card should have name, description, location
#
# display vs. ascii
#
# Against B: card should have name, description, location
#
# ask who has more followers
#
# compare the guesses. If user is correct, continue, else stop


import art
import game_data
import os
import random

def my_input(text, restrictions=[]):
    if restrictions is None:
        restrictions = []
    filtered = False
    input_res = ''
    while not filtered:
        input_res = input(text).strip()
        input_res_lower = input_res.lower()
        if input_res_lower == '':
            print("\nYou didn't enter any text.\n")

        if len(restrictions) > 0:

            if input_res_lower not in restrictions:
                print(f'\nAnswers are restricted to the following: {restrictions}.\n')
            else:
                filtered = True
                break
        else:
            filtered = True
            break
    return input_res


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_random_card(current_name=''):
    card = random.choice(game_data.data)
    while current_name == card['name']:
        card = random.choice(game_data.data)
    return card



def guess_correct(card_a, card_b, guess):
    if (guess == 'a' and card_a > card_b) or (guess == 'b' and card_a < card_b):
        return True
    else:
        return False

def new_a_card(card_a, card_b):
    if card_a['follower_count'] > card_b['follower_count']:
        return [card_a, card_b['name']]
    else:
        return [card_b, card_a['name']]

playing = True
winning = False
current_score = 0
losing_card_name = ''
# continue_with_highest is a custom setting where if True, the game doesn't replace card_a with card_b,
# instead it keeps the highest card until it gets beat, then it replaces the current highest with the new highest.
continue_with_highest = False
while playing:
    clear()
    print(art.logo)
    if winning:
        print(f"You're right! Current score: {current_score}.")
    else:
        card_a = get_random_card()

    card_b = get_random_card(losing_card_name)
    while card_b['name'] == card_a['name']:
        card_b = get_random_card()
    print(f"Compare A: {card_a['name']}, {card_a['description']}, from {card_a['country']}.")
    # print("DEBUG",card_a['follower_count'])
    print(art.vs)
    print(f"Against B: {card_b['name']}, {card_b['description']}, from {card_b['country']}.")
    # print("DEBUG",card_b['follower_count'])

    guess = my_input(f"Who has more followers? Type 'A' or 'B': ", ['A', 'a', 'B', 'b']).lower()
    if guess_correct(card_a['follower_count'], card_b['follower_count'], guess):
        current_score += 1
        winning = True
        if continue_with_highest:
            new_card = new_a_card(card_a, card_b)
            card_a = new_card[0]
            losing_card_name = new_card[1]
        else:
            card_a = card_b
    else:
        clear()
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {current_score}")
        winning = False
        playing = False
        current_score = 0
        break

