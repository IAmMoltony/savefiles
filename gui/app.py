import tkinter as tk
from tkinter import scrolledtext
import backup
from util import stdout_capture
from util import file_opener
from gui import enterbox
from gui import infobox

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

        self.button_view_user = tk.Button(self, text="View user settings", command=self.do_view_user)
        self.button_view_user.pack()

        self.button_edit_user = tk.Button(self, text="Edit user settings", command=self.do_edit_user)
        self.button_edit_user.pack()

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
        print("[App] Doing all-game backup")
        self.clear_cmd_output()
        self.set_buttons_state("disabled")
        cap, old = stdout_capture.start()
        backup.main("backup")
        output = stdout_capture.end(cap, old)
        self.add_cmd_output(output)
        self.set_buttons_state("normal")

    def do_single_backup(self):
        print("[App] Doing single-game backup")
        self.clear_cmd_output()
        self.set_buttons_state("disabled")
        enterbox.EnterBox("What game do you want to back up?", self.single_backup_box_callback, self.single_backup_close_callback)

    def single_backup_box_callback(self, user_input):
        cap, old = stdout_capture.start()
        backup.main("backup", user_input)
        output = stdout_capture.end(cap, old)
        self.add_cmd_output(output)
        self.set_buttons_state("normal")

    def single_backup_close_callback(self):
        self.set_buttons_state("normal")

    def do_view_user(self):
        print("[App] Viewing user settings")
        self.clear_cmd_output()
        self.set_buttons_state("disabled")
        cap, old = stdout_capture.start()
        backup.main("printuser")
        output = stdout_capture.end(cap, old)
        self.add_cmd_output(output)
        self.set_buttons_state("normal")

    def do_edit_user(self):
        print("[App] Editing user settings")
        if not file_opener.open_file("./user.json"):
            infobox.InfoBox("Error: could not open user.json file")

    def set_buttons_state(self, state):
        self.button_single_backup.config(state=state)
        self.button_all_backup.config(state=state)
        self.button_view_user.config(state=state)

