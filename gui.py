import tkinter as tk
from threading import Thread
from tkinter import filedialog

import cv2
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

from defense import AttackDefense


class DemoGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("對縮放攻擊的防禦GUI by Jun Hu")
        self.pack()
        self._create_widgets()

    def onOpen(self):
        filename = filedialog.askopenfilename()
        if filename:
            size = tuple(map(int, self.size_var.get().split("x")))
            self.atkdfn.load_img(filename)
            self.atkdfn.run(size)
            self.canvas.draw()

    def _create_widgets(self):
        self.size_var=tk.StringVar()

        button = tk.Button(self, text="餵圖片喇", fg="blue", command=self.onOpen)
        button.pack(side="top")
        frame = tk.Frame(self)
        frame.pack(side="top")
        name_label = tk.Label(frame, text='欲防禦之攻擊大小')
        name_label.pack(side="left")
        size_entry = tk.Entry(frame, textvariable=self.size_var)
        size_entry.pack(side="left")
        size_entry.insert(0, "258x258")

        fig = Figure(figsize=(20, 4))
        self.atkdfn = AttackDefense("jb.jpg", fig)
        self.atkdfn.run((258, 258))

        self.canvas = FigureCanvasTkAgg(fig, self)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side="top", fill=tk.BOTH, expand=1)

        self.quit = tk.Button(self, text="離開啊 哪次不離開", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")


if __name__ == '__main__':
    root = tk.Tk()
    app = DemoGUI(master=root)
    app.mainloop()
