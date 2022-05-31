import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.questions_list = questions
        self.score = 0

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text} (True/False)? ").lower()
        self.check_answer(answer, question.answer)

    def still_has_questions(self):
        return self.question_number + 1 <= len(self.questions_list)

    def check_answer(self, u_anser, correct_answer):
        if u_anser == correct_answer.lower():
            self.score += 1
            print(f"You got it right!")
        else:
            print(f"Sorry, you got it wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f" Your score is: {self.score}/{self.question_number}")
