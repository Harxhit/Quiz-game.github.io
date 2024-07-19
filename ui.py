from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Creates Canvas 
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.questions_text = self.canvas.create_text(150, 125, text="Some question", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=50, pady=50)

        # Load images for the buttons
        false_image = PhotoImage(file="C:\\Users\\Welcome\\OneDrive\\Desktop\\Python\\Mini Project\\API\\Quizzler\\images\\false.png")
        true_image = PhotoImage(file="C:\\Users\\Welcome\\OneDrive\\Desktop\\Python\\Mini Project\\API\\Quizzler\\images\\true.png")

        # Create False button
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=0, row=2)
        self.false_button.image = false_image  # Prevent image from being garbage collected

        # Create True button
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=1, row=2)
        self.true_button.image = true_image  # Prevent image from being garbage collected

        # Create Score label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 14, "bold"))
        self.score_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score : {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questions_text, text=q_text)
        else:
            self.canvas.itemconfig(self.questions_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
