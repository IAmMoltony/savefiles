#!/usr/bin/bash

echo "[Auto] Starting automatic backup"
cd "$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
./backup.py backup
git add saves
git commit -m "Automatic backup: $(date +"%F %T")"
git push
