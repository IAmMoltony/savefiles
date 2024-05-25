from backupper import Backupper


class BabaIsYouBackupper(Backupper):
    def __init__(self, paths: dict[str], machine_name: str):
        super().__init__(paths, machine_name, "BabaIsYou")

    def backup(self):
        self.copyall()
