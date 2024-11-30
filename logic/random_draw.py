import random
import json
from tkinter import messagebox
from hashlib import sha256
from logic.configure import config


class CertificationErrow(Exception):

    def __init__(self, message: str):
        self.message = message

    pass


def draw_random_student():
    conf = config()
    # 认证
    with open(str(conf.get("paths.students_path")), 'rb') as file:
        if conf.get("certification"):
            file_content = file.read()  # 读取文件内容
            if conf.get("certification") != sha256(file_content).hexdigest():
                # print(sha256(file_content).hexdigest())
                raise CertificationErrow("The SHA-256 values ​​of the files do not match.")
    with open(str(conf.get("paths.students_path")), 'r',
              encoding='utf-8') as file:
        students = json.load(file)
    student_id = random.choice(students)
    messagebox.showinfo("抽取结果", f"抽中的学生: {student_id}")
