import time
import tkinter as tk
from tkinter import ttk
from gui.components import create_schedule_entries, create_buttons
from logic.scheduler import scheduler
from logic.random_draw import draw_random_student
from logic.configure import config


class MainWindow:
    __conf = config()
    __schedule = scheduler(__conf.get("paths.schedule_path"))

    def __init__(self, master):

        self.master = master
        self.master.title("课程表")

        fonts = self.__conf.get("fonts")
        WINDOW_WIDTH = self.__conf.get("window_width")

        self.master.overrideredirect(True)
        self.master.geometry(
            f"{WINDOW_WIDTH}x{self.master.winfo_screenheight()}+{self.master.winfo_screenwidth() - WINDOW_WIDTH}+0"
        )

        self.title_label = tk.Label(master,
                                    text="课程表",
                                    font=tuple(fonts["title_font"]))
        self.title_label.pack(pady=10)

        self.time_label = tk.Label(master,
                                   text="",
                                   font=tuple(fonts["time_font"]),
                                   fg="blue")
        self.time_label.pack(pady=10)

        self.entries = create_schedule_entries(5, master)
        ttk.Separator(master, orient="horizontal").pack(fill="x",
                                                        padx=20,
                                                        pady=10)
        self.entries += create_schedule_entries(3, master)
        ttk.Separator(master, orient="horizontal").pack(fill="x",
                                                        padx=20,
                                                        pady=10)
        self.entries += create_schedule_entries(3, master)

        self.upper_var = tk.IntVar()
        upper_checkbox = tk.Checkbutton(master,
                                        text="置顶窗口",
                                        variable=self.upper_var,
                                        command=self.switch_upper)
        upper_checkbox.pack()

        create_buttons(master, self.save_schedule, draw_random_student)

        self.update_time()
        self.update_schedule()

    def switch_upper(self):
        if self.upper_var.get() == 1:
            self.master.attributes('-topmost', 'true')
        else:
            self.master.attributes('-topmost', 'false')

    def update_time(self):
        self.time_label.config(text=time.strftime("%Y-%m-%d\n%H:%M:%S"))
        self.master.after(1000, self.update_time)

    def update_schedule(self):
        self.__schedule.load(time.strftime("%A"), self.entries)
        self.master.after(1000 * 60, self.update_time)

    def save_schedule(self):
        self.__schedule.save(day=time.strftime("%A"), entries=self.entries)
