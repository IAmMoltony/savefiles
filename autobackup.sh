#!/usr/bin/bash

echo "[Auto] Starting automatic backup"
./backup.py backup
git add saves
git commit -m "Automatic backup: $(date +"%F %T")"
git push
