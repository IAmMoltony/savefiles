from backupper import Backupper, BackupperError
import os


class MinecraftBackupper(Backupper):
    def __init__(self, paths: dict[str], machine_name: str, config: dict):
        super().__init__(paths, machine_name, "Minecraft", config)

    def backup(self):
        saves = self.listdir("saves")
        saves_clean = []
        for save in saves:
            if save in self.config["IgnoreWorlds"]:
                print(f"[{self.game_name}] World '{save}' ignored")
            else:
                saves_clean.append(save)

        for save in saves_clean:
            self.copydir(os.path.join("saves", save))
