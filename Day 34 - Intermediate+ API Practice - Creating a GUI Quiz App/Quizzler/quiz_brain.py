import html
from question_model import Question
from data import question_data


class QuizBrain:

    def __init__(self):
        self.question_list = []
        self.question_number = 0
        self.score = 0
        self.get_new_questions()
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {html.unescape(self.current_question.text)}"

    def check_answer(self, user_answer):
        correct_answer = bool(self.current_question.answer)
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False

        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")
    def get_new_questions(self):
        self.question_list.clear()
        for question in question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            self.question_list.append(new_question)
