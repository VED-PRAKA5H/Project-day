from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question = data["question"]
    answer = data["correct_answer"]
    question_bank.append(Question(question, answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print("you have completed the quiz.")
print(f"your final score was: {quiz.score}/{quiz.questionnumber}")

