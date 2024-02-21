import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_data_dict = {row.letter: row.code for (index, row) in pandas.read_csv('./nato_phonetic_alphabet.csv').iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    text = input('Input text: ').upper()
    print([nato_data_dict[char] for char in text if char in nato_data_dict])

