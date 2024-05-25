
# savefiles

This is my repository for backing up game save files.

## Usage

### Initial installation

Copy `user_EXAMPLE.json` as `user.json` in the repository directory. Then fill in
your game paths (see below) and your machine name (used for separating different
machines' save file backups).

### Actual usage

There are two back-up modes: *all-game* and *single-game* backups.

An all-game backup backs up every single game. To perform one, simply do
`./backup.py backup`.

A single-game backup backs up just one game that you want to back up. To perform
one, do `./backup.py backup -g (game name here)`

## Supported games

- Minecraft (`Minecraft`)
- Touhou 6: the Embodiment of Scarlet Devil (`Touhou06`)
- Touhou 7: Perfect Cherry Blossom (`Touhou07`)
- Baba Is You (`BabaIsYou`)
- Super Tux (`SuperTux`)

If you'd like to request support for a game, don't hesitate to open a GitHub
issue about it.

## Adding support for new games

Adding support for new games is quite simple.

1. Create a `backupper_game.py`, replace `game` with the name of the game.
1. Add the following code (do not forget to replace the game name):
    ```python
    from backupper import Backupper

    class GameBackupper(Backupper): # <-- Replace the game name!
        def __init__(self, paths: dict[str], machine_name: str):
            super().__init__(paths, machine_name, "GameName") # <-- Replace the game name!

        def backup(self):
            # This is where the actual backup procedure happens
            # Example:
            self.copyall() # Copy all files from the save directory to the repo
            # See section "API reference" below
    ```
1. Add your backupper to `backuppers.py`:
    1. Add an import line at the top (replace the game name):
        ```python
        from backupper_game import GameBackupper
        ```
    1. Add it to the list of backuppers (do not forget to replace the game name):
        ```python
        BACKUPPERS = {
            # ... other games ...
            "GameName": GameBackupper
        }
        ```
1. Optionally, add it to `user.json`.

## API reference

There are multiple functions for save file backup.

---

```python
self.copyall()
```

Copy anything and everything from the save file folder.

Example:

```python
def backup(self):
    self.copyall() # copy everything!!!
```

---

```python
self.copydir(directory)
```

Copy a specific directory from the save file folder.

Example:

```python
def backup(self):
    self.copydir("replay") # Copy all files from the replay folder
```

---

```python
self.copydirwc(pattern)
```

Copy directories from the save file directory that follow a certain pattern.

Example:

```python
def backup(self):
    self.copydirwc("profile*") # Copy all directories that start with `profile`
```

---

```python
self.copyfile(file)
```

Copy a specific file from the save file directory.

Example:

```python
def backup(self):
    self.copyfile("score.txt") # Copy score.txt and nothing else
```
