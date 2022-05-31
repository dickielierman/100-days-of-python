#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('Input/Names/invited_names.txt') as f:
    list_of_names = f.read().split('\n')

with open('Input/Letters/starting_letter.txt') as f:
    boilerplate = f.read()

for person in list_of_names:
    with open(f'Output/ReadyToSend/invitation-for-{person.lower()}.txt', mode='w') as f:
        f.write(boilerplate.replace('[name]', person))
