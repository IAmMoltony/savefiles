from backupper import Backupper


class SuperTuxBackupper(Backupper):
    def __init__(self, paths: dict[str], machine_name: str):
        super().__init__(paths, machine_name, "SuperTux")

    def backup(self):
        self.copydirwc("profile*")
