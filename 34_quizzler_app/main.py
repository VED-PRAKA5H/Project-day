from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
question_bank = []


for data in question_data:
    question = data["question"]
    answer = data["correct_answer"]
    question_bank.append(Question(question, answer))

quiz = QuizBrain(question_bank)

QuizInterface(quiz)
