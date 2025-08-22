# ColoState Machine Info (Minfo)
A python module to fetch usage information on Colorado State's linux machines.
Tested using python 3.12.

## Installation
Minfo can be installed using pip:
```
pip install git+https://github.com/jschott515/colostate-minfo.git
```

# Minfo Tools

## `launch_ssh`
Launches an SSH session using the machine with the lowest CPU utilization.
Assumes that `ssh` is on the PATH. Alternatively, the path can be passed via command line.

### Usage
- `python -m minfo.tools.launch_ssh <CSU NetID>`

For help:
- `python -m minfo.tools.launch_ssh --help`


### Vscode Integration
A terminal profile can be created for vscode as follows:
```json
    "terminal.integrated.profiles.windows": {
        "ColoState": {
            "path": "python",
            "args": [
                "-m",
                "minfo.tools.launch_ssh",
                "<CSU NetID>",
            ],
        },
    },
```

## `launch_vscode`
Launches a Vscode Remote SSH session using the machine with the lowest CPU utilization. Opens the remote machine's home directory by default.
Assumes that the Remote SSH extension is installed in vscode.
Assumes that `code.cmd` is on the PATH. Alternatively, the path can be passed via command line.

### Usage
- `python -m minfo.tools.launch_vscode <CSU NetID>`

For help:
- `python -m minfo.tools.launch_vscode --help`

### Desktop Shortcut
A desktop shortcut can be made by creating a shortcut to pythonw.exe and adding the command line arguments to the target as follows:
![screenshot](docs/images/desktop_shortcut.png)
