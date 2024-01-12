from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_bank.append(Question(i["text"], i["answer"]))

quiz = QuizBrain(question_bank)

quiz.next_question()

print(f"You have completed the Quiz.\nYour final score was {quiz.score}/{quiz.question_number}")