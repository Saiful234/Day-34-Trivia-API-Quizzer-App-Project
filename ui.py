from tkinter import *
from quiz_brain import QuizBrain



THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: ", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)


        self.canvas = Canvas(width=300, height=250, bg="white")
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.question_text = self.canvas.create_text(150, 125, width=280,
                                                     text="Some question are ready",
                                                     font=("Arial", 17, "italic")
                                                     )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_button = Button(image=true_image, bg=THEME_COLOR, highlightthickness=0, command=self.got_correct)
        self.false_button = Button(image=false_image, bg=THEME_COLOR, highlightthickness=0, command=self.got_wrong)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def got_correct(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)

    def got_wrong(self):
        is_wrong = self.quiz.check_answer("False")
        self.give_feedback(is_wrong)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)
