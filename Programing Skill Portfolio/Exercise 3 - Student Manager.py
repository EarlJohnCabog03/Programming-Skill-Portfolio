# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 00:05:44 2024

@author: Earl
"""

import tkinter as tk
from tkinter import messagebox, ttk

# Updated student data with more records
students = [
    {'name': 'Gareth Southgate', 'number': 9384, 'coursework': 19, 'exam': 33},
    {'name': 'Matt Thompson', 'number': 1234, 'coursework': 75, 'exam': 82},
    {'name': 'Alice Walker', 'number': 4321, 'coursework': 62, 'exam': 70},
    {'name': 'Emily Clark', 'number': 5678, 'coursework': 88, 'exam': 91},
    {'name': 'John Doe', 'number': 9876, 'coursework': 55, 'exam': 60},
    {'name': 'Sarah Johnson', 'number': 1357, 'coursework': 70, 'exam': 80},
    {'name': 'James Smith', 'number': 2468, 'coursework': 45, 'exam': 52},
    {'name': 'Olivia Brown', 'number': 1122, 'coursework': 83, 'exam': 77},
    {'name': 'David Wilson', 'number': 3344, 'coursework': 90, 'exam': 94},
    {'name': 'Sophia Martinez', 'number': 5566, 'coursework': 50, 'exam': 48},
    {'name': 'Ethan Lee', 'number': 7788, 'coursework': 60, 'exam': 62}
]

# Function to calculate percentage and grade
def calculate_results(student):
    total = student['coursework'] + student['exam']
    percentage = (total / 160) * 100
    if percentage >= 70:
        grade = 'A'
    elif percentage >= 60:
        grade = 'B'
    elif percentage >= 50:
        grade = 'C'
    elif percentage >= 40:
        grade = 'D'
    else:
        grade = 'F'
    return percentage, grade

# Function to view all student records
def view_all_records():
    records = ""
    for student in students:
        percentage, grade = calculate_results(student)
        records += (f"Name: {student['name']}\n"
                    f"Number: {student['number']}\n"
                    f"Coursework Total: {student['coursework']}\n"
                    f"Exam Mark: {student['exam']}\n"
                    f"Overall Percentage: {percentage:.2f}%\n"
                    f"Grade: {grade}\n\n")
    messagebox.showinfo("All Student Records", records)

# Function to display individual student record
def view_student_record():
    selected_student = student_combo.get()
    if not selected_student:
        messagebox.showwarning("Selection Error", "Please select a student!")
        return
    student = next(s for s in students if s['name'] == selected_student)
    percentage, grade = calculate_results(student)
    output = (f"Name: {student['name']}\n"
              f"Number: {student['number']}\n"
              f"Coursework Total: {student['coursework']}\n"
              f"Exam Mark: {student['exam']}\n"
              f"Overall Percentage: {percentage:.2f}%\n"
              f"Grade: {grade}")
    student_details_label.config(text=output)

# Function to show highest score
def show_highest_score():
    highest_student = max(students, key=lambda s: s['coursework'] + s['exam'])
    view_student(highest_student)

# Function to show lowest score
def show_lowest_score():
    lowest_student = min(students, key=lambda s: s['coursework'] + s['exam'])
    view_student(lowest_student)

# Helper function to view student details
def view_student(student):
    percentage, grade = calculate_results(student)
    output = (f"Name: {student['name']}\n"
              f"Number: {student['number']}\n"
              f"Coursework Total: {student['coursework']}\n"
              f"Exam Mark: {student['exam']}\n"
              f"Overall Percentage: {percentage:.2f}%\n"
              f"Grade: {grade}")
    messagebox.showinfo("Student Record", output)

# Create main application window with unique background color
root = tk.Tk()
root.title("Student Manager")
root.geometry("500x400")
root.configure(bg="#f0f8ff")  # Light blue background

# Title Label
title_label = tk.Label(root, text="Student Manager", font=("Arial", 16), bg="#f0f8ff")
title_label.pack(pady=10)

# Buttons for main actions
btn_frame = tk.Frame(root, bg="#f0f8ff")  # Matching background
btn_frame.pack(pady=10)

view_all_btn = tk.Button(btn_frame, text="View All Student Records", command=view_all_records, width=20, bg="#add8e6", fg="black")
view_all_btn.grid(row=0, column=0, padx=10, pady=5)

highest_score_btn = tk.Button(btn_frame, text="Show Highest Score", command=show_highest_score, width=20, bg="#add8e6", fg="black")
highest_score_btn.grid(row=0, column=1, padx=10, pady=5)

lowest_score_btn = tk.Button(btn_frame, text="Show Lowest Score", command=show_lowest_score, width=20, bg="#add8e6", fg="black")
lowest_score_btn.grid(row=0, column=2, padx=10, pady=5)

# Dropdown menu to select individual student
student_label = tk.Label(root, text="View Individual Student Record:", font=("Arial", 12), bg="#f0f8ff")
student_label.pack(pady=10)

student_combo = ttk.Combobox(root, values=[s['name'] for s in students], state="readonly", width=20)
student_combo.pack()

view_record_btn = tk.Button(root, text="View Record", command=view_student_record, bg="#add8e6", fg="black")
view_record_btn.pack(pady=5)

# Label to display student details
student_details_label = tk.Label(root, text="", font=("Arial", 10), justify="left", bg="#f0f8ff")
student_details_label.pack(pady=10)

# Run the tkinter event loop
root.mainloop()
