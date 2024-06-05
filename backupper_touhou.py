from backupper import Backupper


class TouhouBackupper(Backupper):
    def __init__(self, paths: dict[str], machine_name: str, touhou_name: str, new = False):
        super().__init__(paths, machine_name, f"Touhou{touhou_name}")
        self.new = new
        self.touhou_name = touhou_name

    def backup(self):
        if self.new:
            self.copydir("replay")
            self.copyfile(f"scoreth{self.touhou_name}.dat")
        else:
            self.copydir("replay")
            self.copyfile("score.dat")


class Touhou06Backupper(TouhouBackupper):
    def __init__(self, paths: dict[str], machine_name: str):
        super().__init__(paths, machine_name, "06")

class Touhou07Backupper(TouhouBackupper):
    def __init__(self, paths: dict[str], machine_name: str):
        super().__init__(paths, machine_name, "07")

class Touhou08Backupper(TouhouBackupper):
    def __init__(self, paths: dict[str], machine_name: str):
        super().__init__(paths, machine_name, "08")

class Touhou10Backupper(TouhouBackupper):
    def __init__(self, paths: dict[str], machine_name: str):
        super().__init__(paths, machine_name, "10", True)

class Touhou18Backupper(TouhouBackupper):
    def __init__(self, paths: dict[str], machine_name: str):
        super().__init__(paths, machine_name, "18", True)

