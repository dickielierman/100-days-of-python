from tkinter import *
from tkinter import messagebox
import pandas as pd
from random import shuffle, randint, choice
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password = [choice(letters) for _ in range(randint(8, 10))] + \
               [choice(numbers) for _ in range(randint(2, 4))] + \
               [choice(symbols) for _ in range(randint(2, 4))]
    shuffle(password)
    password = ''.join(password)
    password_input.delete(0, 'end')
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    website = web_input.get().strip()
    user = user_input.get().strip()
    password = password_input.get().strip()
    if website == '' or user == '' or password == '':
        messagebox.showinfo(title="Oops", message="You can't leave empty fields.")
    else:
        save_pass = messagebox.askokcancel(title="Saving a password", message=f"Website: {website}\nUser/Email: {user}\nPassword: {password}\n\nWould you like to save?")
        if save_pass:
            data = {
                'Website': [website],
                'User/Email': [user],
                'Password': [password]
            }
            # Make data frame of above data
            df = pd.DataFrame(data)
            df.to_csv('not-the-passwords.csv', mode='a', index=False, header=False)
            web_input.delete(0, 'end')
            password_input.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #


LONGLABELS = 56
DEFAULT_EMAIL = 'test@email.com'
window = Tk()
window.title("Password Manager")
window.config(padx=80, pady=80)

canvas = Canvas(width=200, height=200, highlightthickness=0)
tomato_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_image)
canvas.grid(column=0, row=0, columnspan=3)

web_label = Label(text="Website:")
web_input = Entry(width=LONGLABELS)
web_label.grid(column=0, row=1, sticky='w')
web_input.grid(column=1, row=1, columnspan=2, sticky='e')
web_input.focus()

user_label = Label(text="Email/Username:")
user_input = Entry(width=LONGLABELS)
user_label.grid(column=0, row=2, sticky='w')
user_input.grid(column=1, row=2, columnspan=2, sticky='e')
user_input.insert(0, DEFAULT_EMAIL)

password_label = Label(text="Password:")
password_input = Entry(width=31)
generate_button = Button(text="Generate Password", width=20, command=gen_pass)
password_label.grid(column=0, row=3, sticky='w')
password_input.grid(column=1, row=3, sticky='e')
generate_button.grid(column=2, row=3, sticky='w')

add_button = Button(text="add", width=63, command=add_pass)
add_button.grid(column=0, row=5, columnspan=3, sticky='w')

# r = Label(bg="red", width=20, height=5)
# r.grid(row=0, column=0)
#
# g = Label(bg="green", width=20, height=5)
# g.grid(row=1, column=1)
#
# b = Label(bg="blue", width=40, height=5)
# b.grid(row=2, column=0, columnspan=2)


window.mainloop()
