class QuizBrain:
    def __init__(self, question_list):
        self.questionnumber = 0
        self.questionlist = question_list
        self.score = 0

    def still_has_question(self):
        if self.questionnumber < len(self.questionlist):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.questionlist[self.questionnumber]
        user_answer = input(f'Q{self.questionnumber +1}. {current_question.text} (True/False): ')
        self.check_answer(user_answer, current_question.answer)
        self.questionnumber += 1

    def check_answer(self, user_ans, q_ans):
        if user_ans.lower() == q_ans.lower():
            self.score += 1
            print(f"You are right.")
        else:
            print("You are wrong")
        print(f"correct answer is {q_ans}.\nYour current score is {self.score}/{self.questionnumber+1}\n")
