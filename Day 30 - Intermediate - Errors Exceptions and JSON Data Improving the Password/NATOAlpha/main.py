import pandas

nato_data_dict = {row.letter: row.code for (index, row) in pandas.read_csv('nato_phonetic_alphabet.csv').iterrows()}

# My original code has a built in if that only returned results for the characters that are in the nato_data_dict, so it just filtered out nonsense without error
# I'm changing my code to complete this project specifically addressing error handling.
# while True:
#     text = input('Input text: ').upper()
#     print([nato_data_dict[char] for char in text if char in nato_data_dict])

natoing = True
while natoing:
    text = input('Input text: ').upper()
    try:
        result=[nato_data_dict[char] for char in text]
        print(result)
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        natoing = False
