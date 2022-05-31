import os

# Absolute path to the desktop
# FILENAME = 'C:\\Users\\Dickie\\Desktop\\my_file.txt'

# relative path to base of D: drive, the root of this directory
FILENAME = '../../../../my_file.txt'

def read_file():
    with open(FILENAME) as f:
        file_content = f.read()
        print(file_content)
        print("------------")


with open(FILENAME, mode='w') as file:
    file.write('\nThis is a new file')

read_file()

with open(FILENAME, mode='a') as file:
    file.write('\nThis is new text in the file we created.')

read_file()

with open(FILENAME, mode='w') as file:
    file.write('Now we overwrote the file.')

read_file()

os.remove(FILENAME)
