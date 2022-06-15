from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json


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
            new_data = {website: {"email": user, "password": password}}
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                data = new_data
            finally:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            web_input.delete(0, 'end')
            password_input.delete(0, 'end')


# ---------------------------- SEARCH FEATURE ------------------------------- #

def search():
    website = web_input.get().strip()
    if website == '':
        messagebox.showinfo(title="Oops", message="You can't search for nothing.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
            return_data = {key: val for (key, val) in data.items() if key.lower() == website.lower()}
            if return_data:
                for key, val in return_data.items():
                    messagebox.showinfo(title=f"Website: {key}", message=f"User/Email: {val['email']} \nPassword: {val['password']}")
                    web_input.delete(0, 'end')
            else:
                messagebox.showinfo(title="Oops", message=f"No dada found for the website: \n'{website}'. \nPlease check your spelling and try again.")
                web_input.delete(0, 'end')

        except FileNotFoundError:
            messagebox.showinfo(title="Oops", message="File not found.")


def search_by_button(website):
    web_input.delete(0, 'end')
    web_input.insert(0, website)
    search()


# ---------------------------- UI SETUP ------------------------------- #


DEFAULT_EMAIL = 'test@email.com'
window = Tk()
window.title("Password Manager")
window.config(padx=80, pady=80)

canvas = Canvas(width=200, height=200, highlightthickness=0)
tomato_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_image)
canvas.grid(column=0, row=0, columnspan=3)

web_label = Label(text="Website:")
web_input = Entry(width=31)
web_label.grid(column=0, row=1, sticky='w')
web_input.grid(column=1, row=1, sticky='e')
web_input.focus()

search_button = Button(text="Search", width=20, command=search)
search_button.grid(column=2, row=1, sticky='w')

user_label = Label(text="Email/Username:")
user_input = Entry(width=56)
user_label.grid(column=0, row=2, sticky='w')
user_input.grid(column=1, row=2, columnspan=2, sticky='e')
user_input.insert(0, DEFAULT_EMAIL)

password_label = Label(text="Password:")
password_input = Entry(width=31)
generate_button = Button(text="Generate Password", width=20, command=gen_pass)
password_label.grid(column=0, row=3, sticky='w')
password_input.grid(column=1, row=3, sticky='e')
generate_button.grid(column=2, row=3, sticky='w')

add_button = Button(text="Add Password", width=69, command=add_pass)
add_button.grid(column=0, row=5, columnspan=3, sticky='w')
no_records_found_label = Label(text="No records found")

# This begins my custom code to create buttons for each
start_stored_passwords_row = 6
bullet = "\u2022"
list_of_websites = []

try:
    with open("data.json", "r") as data_file:
        pw_data = json.load(data_file)
    if pw_data:
        website_header = Label(text="\nPasswords Available For\n")
        website_header.grid(column=0, row=start_stored_passwords_row, columnspan=3)
        start_stored_passwords_row += 1
        counted_items = 0
        total_items = 0
        for website, credentials in pw_data.items():
            list_of_websites.append(total_items)
            stored_pass = Button(text=website, width=20, command=lambda m=f"{website}": search_by_button(m))
            stored_pass.grid(column=counted_items, row=start_stored_passwords_row)
            counted_items += 1
            total_items += 1
            if counted_items % 3 == 0:
                counted_items = 0
                start_stored_passwords_row += 1

    else:
        no_records_found_label.grid(column=0, row=start_stored_passwords_row, sticky='w', columnspan=3)
except FileNotFoundError:
    no_records_found_label.grid(column=0, row=start_stored_passwords_row, sticky='w', columnspan=3)

window.mainloop()
