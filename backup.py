#!/usr/bin/python3

import argparse
import os
import sys
import gui
import util
from user import User
from backuppers import BACKUPPERS
from backupper import Backupper

__version__ = "1.6"


def main(action: str, game_name: str = None, dry: bool = False):
    if not os.path.exists("./user.json"):
        print("user.json not found, please create")
        return False

    user = User()
    user.load()

    Backupper.dry_run = dry
    if dry:
        print("[Backup] Dry-run enabled, not making any changes")

    if action == "version":
        print(f"Backup.py version {__version__}")
        return True
    elif action == "printuser":
        print(user)
        return True
    elif action == "backup":
        print("[Backup] Back up started")
        print(user)

        backupper_classes = []
        for game in user.paths.keys():
            if game in BACKUPPERS:
                backupper_classes.append(BACKUPPERS[game])
        print(f"[Backup] Available backuppers for this computer: {backupper_classes}")

        backupper_objects = []
        for cls in backupper_classes:
            try:
                backupper_objects.append(cls(user.paths, user.machine_name, user.config))
            except TypeError:
                backupper_objects.append(cls(user.paths, user.machine_name))

        if game_name is not None:
            game_backupper = None
            for obj in backupper_objects:
                if obj.game_name == game_name:
                    game_backupper = obj
                    break
            if game_backupper is None:
                print(
                    f"[Backup] Could not find backupper for game '{game_name}' or game not registered in user.json"
                )
                return False
            else:
                game_backupper.backup()
                print("[Backup] Single-game backup done")
                return True

        for obj in backupper_objects:
            obj.backup()
        print("[Backup] All-game backup done")
        return True
    elif action == "gui":
        gui.start_gui()
        return True
    return True

def set_wd():
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    os.chdir(script_dir)


def entry():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action",
        type=str,
        choices=["version", "backup", "printuser", "gui"],
        help="what to do",
    )
    parser.add_argument(
        "--game",
        "-g",
        type=str,
        help="when 'backup' action, only backup the specified game",
    )
    parser.add_argument(
        "--dry",
        "-d",
        action="store_true",
        help="when 'backup' action, don't do any actual changes"
    )
    args = parser.parse_args()

    set_wd()

    if not main(args.action, args.game, args.dry):
        sys.exit(1)


if __name__ == "__main__":
    entry()
