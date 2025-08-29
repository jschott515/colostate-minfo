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
    parser.add_argument("--location", "-l", type=str,
                        help="Specify a lab to pick a machine from")
    parser.add_argument("--ssh", type=str, default=SSH_PATH,
                        help="SSH executable path")
    cfg = parser.parse_args(sys.argv[1:])
    return cfg


def get_min_usage_host(info: typing.Sequence[typing.MutableMapping[minfo.MinfoFields, str]]) -> str:
    device_info = min(info, key=lambda x: x[minfo.MinfoFields.CPU_USAGE])
    return device_info[minfo.MinfoFields.HOST]


def filter_machines(info: typing.Sequence[typing.MutableMapping[minfo.MinfoFields, str]],
                    field: minfo.MinfoFields,
                    key: str,
                    ) -> typing.Sequence[typing.MutableMapping[minfo.MinfoFields, str]]:
    filtered_info = list(filter(lambda x: x[field] == key, info))
    if len(filtered_info) == 0:
        raise ValueError(f"No machines available matching {field} `{key}`")
    return filtered_info


def main() -> None:
    cfg = parse_args()
    username = typing.cast(str, cfg.USERNAME)
    location = typing.cast(str | None, cfg.location)
    ssh_path = typing.cast(str, cfg.ssh)

    info = minfo.fetch_machine_info()
    if location is not None:
        info = filter_machines(info, minfo.MinfoFields.LOCATION, location)
    machine = get_min_usage_host(info)
    target = TARGET.format(username=username, machine=machine)
    subprocess.run([ssh_path, target])


if __name__ == "__main__":
    sys.exit(main())
