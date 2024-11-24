import random
import json
from tkinter import messagebox

def draw_random_student():
    with open('students.json', 'r', encoding='utf-8') as file:
        students = json.load(file)
    student_id = random.choice(students)
    messagebox.showinfo("抽取结果", f"抽中的学生 ID: {student_id}")
