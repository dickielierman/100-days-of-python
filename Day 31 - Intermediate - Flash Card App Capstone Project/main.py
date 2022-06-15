from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pandas as pd


def random_card():
    global timer
    global current_card
    if timer != None:
        window.after_cancel(timer)
    current_card = choice(CARDS)
    canvas.itemconfig(canvas_image, image=card_image_one)
    canvas.itemconfig(word_text, text=current_card['French'], fill='black')
    canvas.itemconfig(language_text, text='French', fill='black')
    timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(word_text, text=current_card['English'], fill='white')
    canvas.itemconfig(language_text, text='English', fill='white')
    canvas.itemconfig(canvas_image, image=card_image_two)


def known():
    global CARDS
    CARDS.remove(current_card)
    df = pd.DataFrame(CARDS)
    df.to_csv('data/words_to_learn.csv', index=False)
    random_card()


def unknown():
    random_card()

# , font=(FONT_NAME, 35, "bold")

current_card = {}
BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')
    data.to_csv('data/words_to_learn.csv', index=False)
data = pd.read_csv('data/words_to_learn.csv')
CARDS = data.to_dict(orient='records')
timer = None
print(CARDS)
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image_one = PhotoImage(file="images/card_front.png")
card_image_two = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(800 / 2, 526 / 2, image=card_image_one)
language_text = canvas.create_text(800 / 2, 150, text="Title", font=('Arial', 40, "italic"))
word_text = canvas.create_text(800 / 2, 253, text="Word", font=('Arial', 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

known_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_image, highlightthickness=0, bd=0, command=known)
known_button.grid(column=1, row=1)

unknown_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, bd=0, command=unknown)
unknown_button.grid(column=0, row=1)
random_card()
window.mainloop()
