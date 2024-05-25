import tkinter as tk

class EnterBox(tk.Tk):
    def __init__(self, prompt, callback_ok, callback_close):
        super().__init__()

        self.resizable = False
        self.attributes("-type", "dialog")
        self.title("Question")

        self.user_input = tk.StringVar()
        self.callback = callback_ok
        self.user_close_callback = callback_close

        tk.Label(self, text=prompt).pack()
        self.input_box = tk.Entry(self)
        self.input_box.bind("<Return>", self.click_callback)
        self.input_box.pack()
        tk.Button(self, text="OK", command=self.click_callback).pack()

        self.protocol("WM_DELETE_WINDOW", self.close_callback)

    def click_callback(self, useless = None): # the useless param is not used
        str_input = self.input_box.get()
        self.destroy()
        self.callback(str_input)

    def close_callback(self):
        self.user_close_callback()
        self.destroy()

