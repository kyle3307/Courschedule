import json
from tkinter import messagebox, END

def load_day_schedule(day, morning_entries, afternoon_entries, evening_entries):
    with open('schedule.json', 'r', encoding='utf-8') as file:
        schedule = json.load(file)

    if day not in schedule:
        messagebox.showerror("错误", f"课程表中没有 '{day}' 的数据！")
        return

    fill_entries(morning_entries, schedule[day].get("Morning", []))
    fill_entries(afternoon_entries, schedule[day].get("Afternoon", []))
    fill_entries(evening_entries, schedule[day].get("Evening", []))

def save_day_schedule(day, morning_entries, afternoon_entries, evening_entries):
    with open('schedule.json', 'r', encoding='utf-8') as file:
        schedule = json.load(file)

    schedule[day] = {
        "Morning": [entry.get() for entry in morning_entries],
        "Afternoon": [entry.get() for entry in afternoon_entries],
        "Evening": [entry.get() for entry in evening_entries],
    }

    with open('schedule.json', 'w', encoding='utf-8') as file:
        json.dump(schedule, file, ensure_ascii=False, indent=4)
    messagebox.showinfo("保存成功", f"课程表已保存到 '{day}'！")

def fill_entries(entries, values):
    for entry, value in zip(entries, values):
        entry.delete(0, END)
        entry.insert(0, value)
