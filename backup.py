#!/usr/bin/python3

import argparse
import os
import sys
from user import User
from backuppers import BACKUPPERS

__version__ = "1.0.1"

def set_wd():
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    os.chdir(script_dir)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", type=str, choices=["version", "backup", "printuser"], help="what to do")
    parser.add_argument("--game", "-g", type=str, help="when 'backup' action, only backup the specified game")
    args = parser.parse_args()

    set_wd()

    if not os.path.exists("./user.json"):
        print("user.json not found, please create")
        sys.exit(1)

    user = User()
    user.load()

    if args.action == "version":
        print(f"Backup.py version {__version__}")
    elif args.action == "printuser":
        print(user)
    elif args.action == "backup":
        print("[Backup] Back up started")
        print(user)

        backupper_classes = []
        for game in user.paths.keys():
            if game in BACKUPPERS:
                backupper_classes.append(BACKUPPERS[game])
        print(f"[Backup] Available backuppers for this computer: {backupper_classes}")

        backupper_objects = []
        for cls in backupper_classes:
            backupper_objects.append(cls(user.paths, user.machine_name))

        if args.game is not None:
            game_backupper = None
            for obj in backupper_objects:
                if obj.game_name == args.game:
                    game_backupper = obj
                    break
            if game_backupper is None:
                print("[Backup] Could not find backupper for game or game not registered in user.json")
                sys.exit(1)
            else:
                game_backupper.backup()
                print("[Backup] Single-game backup done")
                sys.exit(0)

        for obj in backupper_objects:
            obj.backup()
        print("[Backup] All-game backup done")
    else:
        print("ok wtf")

if __name__ == "__main__":
    main()
