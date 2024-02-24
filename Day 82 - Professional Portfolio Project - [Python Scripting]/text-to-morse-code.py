morse_code = {
    'a': '·-', 'b': '-···', 'c': '-·-·', 'd': '-··', 'e': '·', 'f': '··-·',
    'g': '--·', 'h': '····', 'i': '··', 'j': '·---', 'k': '-·-', 'l': '·-··',
    'm': '--', 'n': '-·', 'o': '---', 'p': '·--·', 'q': '--·-', 'r': '·-·',
    's': '···', 't': '-', 'u': '··-', 'v': '···-', 'w': '·--', 'x': '-··-',
    'y': '-·--', 'z': '--··',
    '0': '-----', '1': '·----', '2': '··---', '3': '···--', '4': '····-',
    '5': '·····', '6': '-····', '7': '--···', '8': '---··', '9': '----·'
}

phonetic_alphabet = {
    'a': 'Alpha', 'b': 'Bravo', 'c': 'Charlie', 'd': 'Delta', 'e': 'Echo',
    'f': 'Foxtrot', 'g': 'Golf', 'h': 'Hotel', 'i': 'India', 'j': 'Juliett',
    'k': 'Kilo', 'l': 'Lima', 'm': 'Mike', 'n': 'November', 'o': 'Oscar',
    'p': 'Papa', 'q': 'Quebec', 'r': 'Romeo', 's': 'Sierra', 't': 'Tango',
    'u': 'Uniform', 'v': 'Victor', 'w': 'Whiskey', 'x': 'X-ray', 'y': 'Yankee',
    'z': 'Zulu',
}


def main():
    # Main loop to keep the program running until the user chooses to quit
    while True:
        option_input = ''
        # Loop to get valid user input for the conversion method
        while option_input not in ['m', 'p', 'q']:
            option_input = input('Would you like to render (m)orse code, the (p)honetic alphabet, or (q)uit? ').lower()
            if option_input not in ['m', 'p', 'q']:
                print("Please enter 'm' for Morse code, 'p' for the phonetic alphabet, or 'q' to quit.")
        # If user chooses to quit, exit the program
        if option_input == 'q':
            print("Exiting the program. Goodbye!")
            break
        # Loop for the conversion process
        while True:
            output = ''
            # Get user input for the message to convert
            user_input = input('Enter the message you wish to convert: ').lower()
            # Convert the message based on the selected option
            if option_input == 'm':
                # Conversion for Morse code
                for char in user_input:
                    # Convert character to Morse code if it's a digit or an alphabet letter
                    # Discard special characters except space
                    # Use four spaces for spaces in the message
                    display = f'{morse_code[char]} ' if char.isdigit() or char.isalpha() else '    ' if char == ' ' else ''
                    output = f'{output}{display}'
            else:
                # Conversion for the phonetic alphabet
                for char in user_input:
                    # Use the phonetic alphabet for alphabet letters
                    # Keep digits as they are
                    # Use spaces for spaces in the message
                    # Discard special characters
                    display = char if char.isdigit() or char.isalpha() else char if char == ' ' else phonetic_alphabet[char] if char.isalpha() else ''
                    output = f'{output} {display}'
            # Print the converted message
            print(f"Converted message: {output}")
            # Loop to get user input for continuing or returning to the main menu
            cont = ''
            while cont not in ['c', 'r']:
                cont = input('(C)ontinue using this conversion method or (r)eturn to the main menu? ').lower()
                if option_input not in ['m', 'p', 'q']:
                    print("Please enter 'c' to continue with this method, or 'r' to return to the main menu.")
            # If user chooses to return to the main menu, break out of the conversion loop
            if cont == 'r':
                print("Returning to the main menu.")
                break


if __name__ == "__main__":
    main()
