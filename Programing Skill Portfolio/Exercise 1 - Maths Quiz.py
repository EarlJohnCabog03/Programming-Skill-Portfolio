# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
import random
from tkinter import messagebox

class MathQuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Math Quiz")

        # Variables to hold quiz state
        self.difficulty = 0
        self.score = 0
        self.question_count = 10
        self.current_question = 0

        # Widgets
        self.menu_frame = tk.Frame(self.master)
        self.menu_frame.pack(pady=20)

        self.title_label = tk.Label(self.menu_frame, text="DIFFICULTY LEVEL", font=("Arial", 16))
        self.title_label.pack()

        self.easy_button = tk.Button(self.menu_frame, text="Easy (1)", command=lambda: self.start_quiz(1))
        self.easy_button.pack(pady=5)

        self.moderate_button = tk.Button(self.menu_frame, text="Moderate (2)", command=lambda: self.start_quiz(2))
        self.moderate_button.pack(pady=5)

        self.advanced_button = tk.Button(self.menu_frame, text="Advanced (3)", command=lambda: self.start_quiz(3))
        self.advanced_button.pack(pady=5)

        self.quiz_frame = tk.Frame(self.master)

        self.question_label = tk.Label(self.quiz_frame, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.quiz_frame, font=("Arial", 14))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.quiz_frame, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack(pady=5)

        self.result_label = tk.Label(self.quiz_frame, text="")
        self.result_label.pack(pady=10)

        self.play_again_button = tk.Button(self.quiz_frame, text="Play Again", command=self.play_again)
        self.play_again_button.pack(pady=5)

    def start_quiz(self, difficulty):
        self.difficulty = difficulty
        self.score = 0
        self.current_question = 0
        self.quiz_frame.pack(pady=20)
        self.menu_frame.pack_forget()
        self.ask_question()

    def randomInt(self):
        if self.difficulty == 1:
            return random.randint(0, 9)  # Easy
        elif self.difficulty == 2:
            return random.randint(10, 99)  # Moderate
        elif self.difficulty == 3:
            return random.randint(1000, 9999)  # Advanced

    def decideOperation(self):
        return random.choice(['+', '-'])

    def ask_question(self):
        num1 = self.randomInt()
        num2 = self.randomInt()
        operation = self.decideOperation()

        self.correct_answer = num1 + num2 if operation == '+' else num1 - num2
        self.question_label.config(text=f"{num1} {operation} {num2} = ?")
        self.answer_entry.delete(0, tk.END)
        self.result_label.config(text="")

    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
            if user_answer == self.correct_answer:
                self.score += 10  # Correct on first attempt
                self.result_label.config(text="Correct! You earned 10 points.")
            else:
                user_answer = int(self.answer_entry.get())
                if user_answer == self.correct_answer:  # Check second attempt
                    self.score += 5  # Correct on second attempt
                    self.result_label.config(text="Correct! You earned 5 points.")
                else:
                    self.result_label.config(text=f"Incorrect! The correct answer was: {self.correct_answer}")

            self.current_question += 1
            if self.current_question < self.question_count:
                self.ask_question()
            else:
                self.display_results()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def display_results(self):
        self.question_label.config(text="")
        self.answer_entry.pack_forget()
        self.submit_button.pack_forget()
        self.result_label.config(text=f"Your final score is: {self.score} out of {self.question_count * 10}")
        if self.score >= 90:
            self.result_label.config(text=f"{self.result_label.cget('text')} - Grade: A+")
        elif self.score >= 80:
            self.result_label.config(text=f"{self.result_label.cget('text')} - Grade: A")
        elif self.score >= 70:
            self.result_label.config(text=f"{self.result_label.cget('text')} - Grade: B")
        elif self.score >= 60:
            self.result_label.config(text=f"{self.result_label.cget('text')} - Grade: C")
        elif self.score >= 50:
            self.result_label.config(f"{self.result_label.cget('text')} - Grade: D")
        else:
            self.result_label.config(f"{self.result_label.cget('text')} - Grade: F")

        self.play_again_button.pack(pady=5)

    def play_again(self):
        self.quiz_frame.pack_forget()
        self.menu_frame.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()

