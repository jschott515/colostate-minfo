import argparse
import typing
import subprocess
import sys

import minfo


SSH_PATH = 'ssh'
TARGET = '{username}@{machine}.cs.colostate.edu'


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("USERNAME", type=str,
                        help="Username used for SSH connection")
    parser.add_argument("--ssh", type=str, default=SSH_PATH,
                        help="SSH executable path")
    cfg = parser.parse_args(sys.argv[1:])
    return cfg


def get_min_usage_host(info: typing.Sequence[typing.MutableMapping[str, str]]) -> str:
    device_info = min(info, key=lambda x: x['CPU Usage (%)'])
    return device_info['Hostname']


if __name__ == "__main__":
    cfg = parse_args()
    info = minfo.fetch_machine_info()
    machine = get_min_usage_host(info)
    target = TARGET.format(username=cfg.USERNAME, machine=machine)
    subprocess.run([cfg.ssh, target])
