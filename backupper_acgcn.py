from backupper import Backupper


class AnimalCrossingGCNDolphinBackupper(Backupper): # what a mouthful :)
    def __init__(self, paths: dict[str], machine_name: str, config: dict):
        super().__init__(paths, machine_name, "AnimalCrossingGCNDolphin", config)
 
    def backup(self):
        self.copyfilewc("*-GAFE-DobutsunomoriP_MURA.gci")
