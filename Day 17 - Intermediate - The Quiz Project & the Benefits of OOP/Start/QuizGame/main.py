from question_model import Question
from game_data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

game = QuizBrain(question_bank)
while game.still_has_questions():
    game.next_question()





