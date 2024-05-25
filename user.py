import json
import os

class User:
    def __init__(self):
        self.machine_name = ""
        self.paths = {}

    def load(self):
        with open("./user.json", "r") as user_json:
            user = json.load(user_json)
            self.machine_name = user["MachineName"]
            self.paths = user["Paths"]

        # expand paths
        for game in self.paths:
            path = self.paths[game]
            self.paths[game] = os.path.expandvars(os.path.expanduser(path))

    def __str__(self):
        s = f"[User] Machine Name: {self.machine_name}\n[User] Paths:\n"

        for game, path in self.paths.items():
            s += f"[User] \t{game}: {path}\n"
        s = s[:-1]
        return s
