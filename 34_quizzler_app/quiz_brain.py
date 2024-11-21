import html


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
        self.current_question = self.questionlist[self.questionnumber]
        # escape the HTML Character Entities from question's text which came from API
        question = html.unescape(self.current_question.text)
        self.questionnumber += 1
        return f'Q{self.questionnumber}. {question}'
        # self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_ans:str):
        if user_ans.lower() == self.current_question.answer.lower():
            self.score += 1
            return True
            # print(f"You are right.")
        else:
            return False
            # print("You are wrong")
        # print(f"correct answer is {q_ans}.\nYour current score is {self.score}/{self.questionnumber+1}\n")
