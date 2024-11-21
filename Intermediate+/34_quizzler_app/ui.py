from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizler App")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.question = self.canvas.create_text(150, 125, text="", width=289, font=("Arial", 15, "bold"))
        self.canvas.grid(row=1, column=0, columnspan=2)
        right = PhotoImage(file="images/true.png")
        self.right_btn = Button(image=right, highlightthickness=0, command=self.clicked_true)
        self.right_btn.grid(row=2, column=1, padx=20, pady=20)
        wrong = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=wrong, highlightthickness=0, command=self.clicked_false)
        self.wrong_btn.grid(row=2, column=0, padx=20, pady=20)
        self.label = Label(text="Score: 0", bg=THEME_COLOR, fg='white')
        self.label.grid(row=0, column=1, pady=20)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        if self.quiz.still_has_question():
            self.canvas.itemconfig(self.question, text=self.quiz.next_question(), font=("Arial", 15, "bold"))
        else:
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")
            self.canvas.itemconfig(self.question,
                                   text=f"All questions ended.\nYour final score: {self.quiz.score}/{self.quiz.questionnumber}",
                                   font=("Arial", 20, "bold"))

    def clicked_true(self):
        if self.quiz.check_answer("true"):
            self.window.config(background='green')
            self.label.config(text=f"Score: {self.quiz.score}")
        else:
            self.window.config(background='red')

        # Wait 1000 ms before resetting the color and moving on
        self.window.after(1000, self.give_feedback)


    def clicked_false(self):
        if self.quiz.check_answer("false"):
            self.window.config(background='green')
            self.label.config(text=f"Score: {self.quiz.score}")
        else:
            self.window.config(background='red')
        self.window.after(1000, self.give_feedback)

    def give_feedback(self):
        self.window.config(background=THEME_COLOR)
        self.next_question()
