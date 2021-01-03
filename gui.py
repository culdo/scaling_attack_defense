import tkinter as tk
from tkinter import filedialog

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


class DemoGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("對縮放攻擊的防禦GUI by Jun Hu")
        self.pack()
        self.create_widgets()

        self.canvas.mpl_connect("key_press_event", self.on_key_press)

    def on_key_press(self, event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, self.canvas, self.toolbar)

    def onOpen(self):
        self.filename = filedialog.askopenfilename()

    def create_widgets(self):

        button = tk.Button(self, text="餵圖片喇", command=self.onOpen)
        button.pack(side="top")

        fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

        self.canvas = FigureCanvasTkAgg(fig, self)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side="top", fill=tk.BOTH, expand=1)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side="top", fill=tk.BOTH, expand=1)

        self.quit = tk.Button(self, text="離開啊 哪次不離開", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

if __name__ == '__main__':
    root = tk.Tk()
    app = DemoGUI(master=root)
    app.mainloop()
