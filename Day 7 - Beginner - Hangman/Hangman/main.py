from my_funcs import clear, pause
import random
import hangman_words
import hangman_art
lives = 6
end_of_game = False
word = random.choice(hangman_words.word_list)
print(word)
display = []
for i in word:
    display.append("_")
won = False
# Start Game
print(hangman_art.logo)
print("The solution is "+word)
previous_guesses = []
while not end_of_game:
    guess = input('Guess a letter: ').lower()
    if guess in previous_guesses:
        print()
        print(f"You've already guessed {guess}.")
        pause(1)
    else:
        previous_guesses.append(guess)
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        if guess not in word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            if lives == 0:
                end_of_game = True
                print(hangman_art.stages[lives])
                print("You lose")
                break
    clear()
    print(display)
    print(hangman_art.stages[lives])
    if '_' not in display:
        end_of_game = True
        print('You won!')


