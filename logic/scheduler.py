import json
from tkinter import messagebox, END


class scheduler:
    __schedule = dict()

    def __init__(self, path: str):
        with open(path, 'r', encoding='utf-8') as file:
            self.__path = path
            self.__schedule = json.load(file)

    def __fill_entries(self, entries, values):
        for entry, value in zip(entries, values):
            entry.delete(0, END)
            entry.insert(0, value)

    def get(self, day=""):
        if not day:
            return self.__schedule
        else:
            if day not in self.__schedule:
                messagebox.showerror("错误", f"课程表中没有 '{day}' 的数据！")
                raise KeyError("Not schedule data of '{day}'.")
                return
            return self.__schedule.get(day)

    def load(self, day, entries):
        self.__fill_entries(entries, self.get(day))

    def save(self, entries, day=""):
        with open(self.__path, 'r', encoding='utf-8') as file:
            schedule = json.load(file)
        schedule[day] = [entry.get() for entry in entries],
        with open('schedule.json', 'w', encoding='utf-8') as file:
            json.dump(schedule, file, ensure_ascii=False, indent=4)
        messagebox.showinfo("保存成功", f"课程表已保存到 '{day}'！")

    pass
