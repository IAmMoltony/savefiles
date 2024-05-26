from backupper import Backupper

class ForagerBackupper(Backupper):
    def __init__(self, paths: dict[str], machine_name: str):
        super().__init__(paths, machine_name, "Forager")

    def backup(self):
        self.copyfile("secretSettings.ini")
        self.copydir("saveData0")
