import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


# Write your code below this line 👇
def rpsChoiceText(val):
    if val == 0:
        return 'ROCK'
    elif val == 1:
        return 'PAPER'
    elif val == 2:
        return 'SCISSORS'


def did_you_win(pc, npc):
    keys = [1, 2, 0]
    if keys[pc] != npc:
        return True
    else:
        return False

player_wins = 0
npc_wins = 0
total_wins = 0
options = [rock, paper, scissors]
while total_wins < 3:
    player = input('1 = rock, 2 = paper, 3 = scissors')
    while not (player == "1" or player == "2" or player == "3"):
        print()
        player = input('1 = rock, 2 = paper, 3 = scissors')
    player = int(player)-1
    print("Player chooses:", rpsChoiceText(player))
    print(options[player])
    pc_choice = random.randint(0, 2)
    print("Computer Player chooses:", rpsChoiceText(pc_choice))
    print(options[pc_choice])
    if player == pc_choice:
        print("It's a draw")
    elif did_you_win(player, pc_choice):
        print("You win!")
        player_wins += 1
        total_wins += 1
    else:
        print("You lose")
        npc_wins += 1
        total_wins += 1
if player_wins > npc_wins:
    print('you won best of three!')
else:
    print('you lost best of three')



