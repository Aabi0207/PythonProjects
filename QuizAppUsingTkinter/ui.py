from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.user_answer = None
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, width=300, text=quiz.next_question(), font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text=f"Score:{self.quiz.score}", fg="white", font=("Arial", 15), bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

    def check_answer(self):
        def change_background():
            self.canvas.config(bg="white")
            if self.quiz.still_has_questions():
                self.canvas.itemconfig(self.question, text=self.quiz.next_question())
                self.score_label.config(text=f"Score:{self.quiz.score}")
            else:
                self.canvas.itemconfig(self.question, text=f"You have completed the quiz you final score is"
                                                           f" {self.quiz.score}/10")
                self.true_button.config(state="disabled")
                self.false_button.config(state="disabled")

        if self.quiz.check_answer(self.user_answer):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, change_background)



    def true(self):
        self.user_answer = "True"
        self.check_answer()

    def false(self):
        self.user_answer = "False"
        self.check_answer()
