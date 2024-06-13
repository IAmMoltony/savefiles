# User configuartion

This is documentation for the `user.json` file.

## Required options

These options have to be set, otherwise the backup script will not work.

### `MachineName`

This is the machine name, used for keeping track of save files on different machines.

### `Paths`

This is a list of paths for each game. Usage of environment variables and `~` is allowed.

Example Usage:

```jsonc
    // ...
    "Paths": {
        "Minecraft": "%appdata%/.minecraft",
        "Touhou07": "~/games/touhou/th07"
    }
    // ...
```

## Optional options

These options allow for extended backup functionality, but they aren't necessary for
the scripts to work.

### `Config`

This is an object storing per-game backup configuration. Usage and supported games can be
found in the "Per-game configuration" section below.

### `AltSaveLocation`

This is an option for specifying a backup path other than `<Repo directory>/saves`. Useful
for backing up to external media or cloud storage (if it's mounted as a drive or directory).

## Per-game configuration

Some games utilize per-game configuration to perform backup differently based on what options
are set in the specific game's configuration.

The following is the syntax of per-game configuration:

```jsonc
    // ...
    "Config": {
        "Game1": {
            "Option": "...",
            "AnotherOption": [
                "Lorem", "Ipsum"
            ]
        },
        "Game2": {
            "OptionOption": 1
        }
    }
    // ...
```

Supported games:

- `Minecraft`

Every per-game configuration option is optional.

### Minecraft configuration

#### `IgnoreWorlds`

A list of worlds that will not be backed up as an array.
