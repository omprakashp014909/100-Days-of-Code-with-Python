from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [ Question(x["text"], x["answer"]) for x in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have answered all questions.")
print(f"Your current score is {quiz.score}/{quiz.question_number }.\n\n")

