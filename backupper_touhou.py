from backupper import Backupper


class TouhouBackupper(Backupper):
    def __init__(self, paths: dict[str], machine_name: str, touhou_name: str):
        super().__init__(paths, machine_name, f"Touhou{touhou_name}")

    def backup(self):
        self.copydir("replay")
        self.copyfile("score.dat")


class Touhou06Backupper(TouhouBackupper):
    def __init__(self, paths: dict[str], machine_name: str):
        super().__init__(paths, machine_name, "06")


class Touhou07Backupper(TouhouBackupper):
    def __init__(self, paths: dict[str], machine_name: str):
        super().__init__(paths, machine_name, "07")
