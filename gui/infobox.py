import tkinter as tk

class InfoBox(tk.Tk):
    def __init__(self, text):
        super().__init__()

        self.resizable = False
        self.attributes("-type", "dialog")
        self.title("Information")

        tk.Label(self, text=text).pack()
        tk.Button(self, text="OK", command=self.destroy).pack()

