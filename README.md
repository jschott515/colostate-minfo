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
Fetches current machine info and launches an SSH session using the machine with the lowest CPU utilization.
Assumes that `ssh` is on the PATH. Alternatively, the path can be passed via command line.

### Usage
- `python -m minfo.tools.launch_ssh <CSU NetID>`

For help:
- `python -m minfo.tools.launch_ssh --help`


# Vscode Integration
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