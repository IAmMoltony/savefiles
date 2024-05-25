from backupper import Backupper


class MinecraftBackupper(Backupper):
    def __init__(self, paths: dict[str], machine_name: str):
        super().__init__(paths, machine_name, "Minecraft")

    def backup(self):
        self.copydir("saves")
