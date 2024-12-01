import tkinter as tk
from logic.configure import config


def create_schedule_entries(periods, parent):
    conf = config()
    fonts = conf.get("fonts")
    entries = []
    for _ in range(periods):
        entry = tk.Entry(parent,
                         font=tuple(fonts["lessons_font"]),
                         justify="center")
        entry.pack()
        entries.append(entry)
    return entries


def create_buttons(parent, save_callback, draw_callback):
    conf = config()
    fonts = conf.get("fonts")
    save_button = tk.Button(parent,
                            text="保存",
                            font=tuple(fonts["button_font"]),
                            command=save_callback)
    save_button.pack(pady=5)

    draw_button = tk.Button(parent,
                            text="抽取",
                            font=tuple(fonts["button_font"]),
                            command=draw_callback)
    draw_button.pack(pady=5)

    close_button = tk.Button(parent,
                             text="关闭",
                             font=tuple(fonts["button_font"]),
                             command=parent.quit)
    close_button.pack(pady=20)
