import tkinter as tk
from tkinter import scrolledtext
import backup
from gui import stdout_capture
from gui import enterbox

class SavefilesApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.resizable = False
        self.attributes("-type", "dialog")

        # set title
        self.title("Savefiles GUI")

        # set icon
        self.iconphoto(False, tk.PhotoImage(file="guiicon.png"))

        self.add_gui_items()

        print("[App] Initialized app")

    def add_gui_items(self):
        self.label_program_name = tk.Label(self, text="Savefiles GUI")
        self.label_program_name.pack()

        self.button_all_backup = tk.Button(self, text="Backup all games", command=self.do_all_backup)
        self.button_all_backup.pack()

        self.button_single_backup = tk.Button(self, text="Backup one game", command=self.do_single_backup)
        self.button_single_backup.pack()

        self.scrolledtext_cmd_output = tk.scrolledtext.ScrolledText(self)
        self.scrolledtext_cmd_output.config(state="disabled")
        self.scrolledtext_cmd_output.pack()

    def add_cmd_output(self, text):
        self.scrolledtext_cmd_output.config(state="normal")
        self.scrolledtext_cmd_output.insert(tk.INSERT, text)
        self.scrolledtext_cmd_output.config(state="disabled")

    def clear_cmd_output(self):
        self.scrolledtext_cmd_output.config(state="normal")
        self.scrolledtext_cmd_output.delete("1.0", tk.END)
        self.scrolledtext_cmd_output.config(state="disabled")

    def do_all_backup(self):
        print(f"[App] Doing all-game backup")
        self.clear_cmd_output()
        self.button_single_backup.config(state="disabled")
        self.button_all_backup.config(state="disabled")
        cap, old = stdout_capture.start()
        backup.main("backup")
        output = stdout_capture.end(cap, old)
        self.add_cmd_output(output)
        self.button_single_backup.config(state="normal")
        self.button_all_backup.config(state="normal")

    def do_single_backup(self):
        print(f"[App] Doing single-game backup")
        self.clear_cmd_output()
        self.button_single_backup.config(state="disabled")
        self.button_all_backup.config(state="disabled")
        enterbox.EnterBox("What game do you want to back up?", self.single_backup_box_callback, self.single_backup_close_callback)

    def single_backup_box_callback(self, user_input):
        cap, old = stdout_capture.start()
        backup.main("backup", user_input)
        output = stdout_capture.end(cap, old)
        self.add_cmd_output(output)
        self.button_single_backup.config(state="normal")
        self.button_all_backup.config(state="normal")

    def single_backup_close_callback(self):
        self.button_single_backup.config(state="normal")
        self.button_all_backup.config(state="normal")

