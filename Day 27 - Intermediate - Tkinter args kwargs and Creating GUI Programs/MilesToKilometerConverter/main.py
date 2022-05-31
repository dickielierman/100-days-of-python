from tkinter import *


def button_clicked():
    result_label["text"] = round(int(input.get()) * 1.60934, 2)


window = Tk()
window.title("Miles to Kilometers")
window.config(padx=80, pady=40)

input = Entry(width=7)
input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="Is equal to")
equal_label.grid(column=0, row=1)

result_label = Label(text="")
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()