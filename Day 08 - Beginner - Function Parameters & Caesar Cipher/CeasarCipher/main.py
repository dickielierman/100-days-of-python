import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = 'encode'
# text = 'zulu'
# shift = 5

# direction = 'decode'
# text = 'ezqz'
# shift = 5


def caesar(text, shift, type):
    if type == 'encode' or type == 'e' or type == 'decode' or type == 'd':
        if type == 'e':
            type = 'encode'
        if type == 'd' or type == 'decode':
            type = 'decode'
            shift *= -1
        result = ''
        for letter in text:
            if letter in alphabet:
                letter_index = alphabet.index(letter)
                new_index = letter_index + shift
                result += alphabet[new_index]
            else:
                result += letter
        print(f'The encoded text is {result}')
    else:
        print("Command not recognized")
continue_using = True
print(art.logo)
while continue_using:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(text, shift, direction)
    print()
    q = input('Would you like to continue?\nEnter "y" or "yes" to continue. Any other input will close the app.\n').lower()
    if q not in ['y','yes']:
        continue_using = False
        break
    print()
