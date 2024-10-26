import os
import json
from typing import List


CONFIG_FILE = "./.config-py-wall.json"


def check_file() -> bool:
    if os.path.isfile(CONFIG_FILE):
        return True
    with open(CONFIG_FILE, mode="w", encoding="utf-8") as write_file:
        json.dump({}, write_file, indent=4)
    check_file()
    return False


def write_config(key: str, value: str | int) -> None:
    check_file()
    with open(CONFIG_FILE, mode="r", encoding="utf-8") as fp:
        configs = json.loads(fp.read())
    configs[key] = value

    with open(CONFIG_FILE, mode="w", encoding="utf-8") as write_file:
        json.dump(configs, write_file, indent=4)


def read_config(key: str):
    check_file()

    with open(CONFIG_FILE, mode="r", encoding="utf-8") as fp:
        configs = json.loads(fp.read())

    if key in configs.keys():
        return configs[key]
    else:
        return False


if __name__ == "__main__":
    write_config("HELLO", "j")
