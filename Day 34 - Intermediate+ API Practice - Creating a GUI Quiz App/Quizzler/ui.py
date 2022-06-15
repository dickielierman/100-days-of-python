from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CORRECT_COLOR = "#bee6c9"
INCORRECT_COLOR = "#dba59e"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", font=("Arial", 12, "italic"), fg='white', bg=THEME_COLOR, padx=0)
        self.score_label.grid(column=1, row=0, sticky='e')

        self.canvas = Canvas(width=300, height=250)
        self.quote_text = self.canvas.create_text(150, 100, text="", width=250, font=("Arial", 16, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, bd=0, command=lambda m=True: self.check_answer(m))
        self.true_button.grid(column=0, row=2, sticky='s')

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, bd=0, command=lambda m=False: self.check_answer(m))
        self.false_button.grid(column=1, row=2, sticky='s')

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.itemconfig(self.quote_text, text=self.quiz.next_question())

    def check_answer(self, is_true: bool):
        if self.quiz.check_answer(is_true):
            self.canvas.config(bg=CORRECT_COLOR)
        else:
            self.canvas.config(bg=INCORRECT_COLOR)

        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.true_button["state"] = "disabled"
        self.false_button["state"] = "disabled"
        self.window.after(2000, self.reset_canvas)

    def reset_canvas(self):
        self.canvas.config(bg='white')
        self.true_button["state"] = "normal"
        self.false_button["state"] = "normal"
        try:
            self.get_next_question()
        except IndexError:
            self.quiz.get_new_questions()
            self.quiz.question_number = 0
            self.get_next_question()


