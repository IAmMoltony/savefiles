from backupper import Backupper


class PeggleBackupper(Backupper):
    def __init__(self, paths: dict[str], machine_name: str):
        super().__init__(paths, machine_name, "Peggle")

    def backup(self):
        self.copydir("userdata")
