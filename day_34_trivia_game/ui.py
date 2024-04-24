from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"


class QuizInterface(QuizBrain):
    def __init__(self, q_list):
        super().__init__(q_list)
        self.window = Tk()
        self.window.title("Trivia Game")
        self.window.config(bg=THEME_COLOR, padx=50, pady=50)

        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, highlightthickness=0,
                                 font=(FONT_NAME, 20, "bold"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=400, height=400, bg="white")

        self.canvas_question = self.canvas.create_text(200, 200, text="", fill="black",
                                                       font=(FONT_NAME, 25, "italic"), justify="center", width=200)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        true_image = PhotoImage(file="images/true.png")
        self.true_response_button = Button(image=true_image, highlightthickness=0, command=self.true_answer)
        self.true_response_button.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.false_response_image = Button(image=false_image, highlightthickness=0, command=self.false_answer)
        self.false_response_image.grid(column=1, row=2)

        self.get_new_question()

        self.window.mainloop()

    def true_answer(self):
        self.check_answer(user_answer="True")
        self.canvas.after(1500, func=self.get_new_question)

    def false_answer(self):
        self.check_answer(user_answer="False")
        self.canvas.after(1500, func=self.get_new_question)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            self.canvas.config(bg="green")
            self.canvas.after(1000, func=self.revert_color)
        else:
            self.canvas.config(bg="red")
            self.canvas.after(800, func=self.revert_color)

        self.score_label.config(text=f"Score: {self.score}")

    def get_new_question(self):

        if self.still_has_questions():
            new_q = self.next_question()
            self.canvas.itemconfig(self.canvas_question, text=f"{new_q}")
        else:
            self.true_response_button.configure(state=DISABLED)
            self.false_response_image.configure(state=DISABLED)
            self.canvas.itemconfig(self.canvas_question,
                                       text=f"Well Done! \n 🎉🎉Game Over 🎉🎉 \n Your score is: {self.score}/{len(self.question_list)}")



    def revert_color(self):
        self.canvas.config(bg="white")
