import os
import shutil
import glob


class BackupperError(Exception):
    pass


class Backupper:
    dry_run = False
    alt_save_location = None

    def __init__(self, paths: dict[str], machine_name: str, game_name: str, config: dict = None):
        self.game_name = game_name
        self.game_path = paths[game_name]

        if self.alt_save_location is not None:
            self.backup_path = os.path.join(self.alt_save_location, machine_name, self.game_name)
        else:
            self.backup_path = os.path.join(".", "saves", machine_name, self.game_name)

        if config is not None and game_name in config:
            self.config = config[game_name]

        try:
            os.makedirs(self.backup_path, exist_ok=True)
        except OSError:
            print(f"[{self.game_name}] Create dir ERROR! See below")
            raise

    def backup(self):
        raise BackupperError("Generic backupper cannot back up any game.")

    def copyall(self):
        print(f"[{self.game_name}] Copy all from {self.game_path}")

        if self.dry_run:
            return

        for item in os.listdir(self.game_path):
            absitem = os.path.join(self.game_path, item)
            destitem = os.path.join(self.backup_path, item)
            isdir = os.path.isdir(absitem)
            file_or_dir = "directory" if isdir else "file"
            print(f"[{self.game_name}] Copying {file_or_dir}: '{item}'")

            if isdir:
                shutil.copytree(absitem, destitem, dirs_exist_ok=True)
            else:
                shutil.copy2(absitem, destitem)

    def copydir(self, directory):
        dir_path = os.path.join(self.game_path, directory)
        dest_path = os.path.join(self.backup_path, directory)
        print(f"[{self.game_name}] Copy directory '{directory}'")

        if self.dry_run:
            return

        try:
            shutil.copytree(dir_path, dest_path, dirs_exist_ok=True)
        except FileNotFoundError:
            print(f"[{self.game_name}] Warning: directory '{directory}' not found, skipping")

    def copydirwc(self, pattern):
        abspattern = os.path.join(self.game_path, pattern)
        print(f"[{self.game_name}] Copy pattern '{pattern}'")

        if self.dry_run:
            return

        for game_dir in glob.glob(abspattern):
            if os.path.isdir(game_dir):
                print(f"[{self.game_name}] Copying directory: '{game_dir}'")
                basename = os.path.basename(game_dir)
                destination = os.path.join(self.backup_path, basename)
                shutil.copytree(game_dir, destination, dirs_exist_ok=True)

    def copyfile(self, file):
        file_path = os.path.join(self.game_path, file)
        dest_path = os.path.join(self.backup_path, file)
        print(f"[{self.game_name}] Copy file '{file}'")

        if self.dry_run:
            return

        shutil.copy2(file_path, dest_path)

    def listdir(self, dir):
        return os.listdir(os.path.join(self.game_path, dir))
