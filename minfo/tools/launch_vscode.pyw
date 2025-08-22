"""Launches a Vscode Remote SSH Session using the machine with the current lowest utilization.
Assumes that the Remote SSH extension is installed.
"""
import argparse
import typing
import subprocess
import sys

import minfo

VSCODE_PATH = 'code.cmd'
TARGET = 'ssh-remote+{username}@{machine}.cs.colostate.edu'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("USERNAME", type=str,
                        help="Username used for remote connection")
    parser.add_argument("--code", type=str, default=VSCODE_PATH,
                        help="Vscode executable path")
    # FUTURE: --dir, specify a remote directory to open
    cfg = parser.parse_args(sys.argv[1:])
    return cfg


def get_min_usage_host(info: typing.Sequence[typing.MutableMapping[minfo.MinfoFields, str]]) -> str:
    device_info = min(info, key=lambda x: x[minfo.MinfoFields.CPU_USAGE])
    return device_info[minfo.MinfoFields.HOST]


if __name__ == "__main__":
    cfg = parse_args()
    username = typing.cast(str, cfg.USERNAME)
    code_path = typing.cast(str, cfg.code)

    info = minfo.fetch_machine_info()
    machine = get_min_usage_host(info)
    target = TARGET.format(username=username, machine=machine)
    subprocess.run([code_path, '--remote', target, '.'])
