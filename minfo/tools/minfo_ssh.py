"""Launches an SSH Session using the machine with the current lowest utilization.
"""
import argparse
import typing
import subprocess
import sys

import minfo


SSH_PATH = 'ssh'
TARGET = '{username}@{machine}.cs.colostate.edu'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("USERNAME", type=str,
                        help="Username used for SSH connection")
    parser.add_argument("--ssh", type=str, default=SSH_PATH,
                        help="SSH executable path")
    cfg = parser.parse_args(sys.argv[1:])
    return cfg


def get_min_usage_host(info: typing.Sequence[typing.MutableMapping[minfo.MinfoFields, str]]) -> str:
    device_info = min(info, key=lambda x: x[minfo.MinfoFields.CPU_USAGE])
    return device_info[minfo.MinfoFields.HOST]


def main() -> None:
    cfg = parse_args()
    username = typing.cast(str, cfg.USERNAME)
    ssh_path = typing.cast(str, cfg.ssh)

    info = minfo.fetch_machine_info()
    machine = get_min_usage_host(info)
    target = TARGET.format(username=username, machine=machine)
    subprocess.run([ssh_path, target])


if __name__ == "__main__":
    sys.exit(main())
