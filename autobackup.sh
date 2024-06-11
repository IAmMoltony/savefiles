#!/usr/bin/bash

if [ ! -z "$1" ]; then
    echo "[Auto] Argument detected"
    if [ "$1" == "ENABLE" ]; then
        echo "[Auto] Enabling autobackup"
        rm -f ~/.savefilesdisabled
    elif [ "$1" == "DISABLE" ]; then
        echo "[Auto] Disabling autobackup"
        touch ~/.savefilesdisabled
    else
        echo "[Auto] Unknown argument $1"
    fi

    exit
fi

if [ -f "$HOME/.savefilesdisabled" ]; then
    echo "[Auto] Autobackup is disabled"
    exit
fi

echo "[Auto] Starting automatic backup"
cd "$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
./backup.py backup
git add saves
git commit -m "Automatic backup: $(date +"%F %T")"
git push
