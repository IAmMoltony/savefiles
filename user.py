import json
import os


class User:
    def __init__(self):
        self.machine_name = ""
        self.paths = {}
        self.config = {}
        self.alt_save_location = None

    def load(self):
        with open("./user.json", "r") as user_json:
            user = json.load(user_json)
            if "MachineName" in user:
                self.machine_name = user["MachineName"]
            else:
                print("[User] MachineName not found!")
                return False
            
            if "Paths" in user:
                self.paths = user["Paths"]
            else:
                print("[User] Paths not found!")
                return False

            if "Config" in user:
                self.config = user["Config"]
            if "AltSaveLocation" in user:
                self.alt_save_location = os.path.expandvars(os.path.expanduser(user["AltSaveLocation"]))

        # expand paths
        for game in self.paths:
            path = self.paths[game]
            self.paths[game] = os.path.expandvars(os.path.expanduser(path))

        return True

    def __str__(self):
        s = f"[User] Machine Name: {self.machine_name}\n[User] Paths:\n"

        for game, path in self.paths.items():
            s += f"[User] \t{game}: {path}\n"

        s += "[User] Config:\n"
        for game, config in self.config.items():
            s += f"[User] \t{game}: {config}\n"

        if self.alt_save_location is not None:
            s += f"[User] Alternative save location: {self.alt_save_location}\n"

        s = s[:-1]
        return s
