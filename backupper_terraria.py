from backupper import Backupper

class TerrariaBackupper(Backupper):
    def __init__(self, paths: dict[str], machine_name: str):
        super().__init__(paths, machine_name, "Terraria")

    def backup(self):
        self.copyfile("achievements.dat")
        self.copyfile("config.json")
        self.copyfile("favorites.json")
        self.copyfile("input profiles.json");
        self.copydir("Players")
        self.copydir("Worlds")
