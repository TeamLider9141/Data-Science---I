#!/usr/bin/env python3
import os
import sys
import subprocess


def check_env():
    env = os.environ.get("VIRTUAL_ENV")
    if not env:
        raise Exception("Script must be run inside the correct virtual environment")


def install_libraries():
    subprocess.run(
        ["pip", "install", "-r", "requirements.txt"],
        check=True
    )


def show_installed():
    result = subprocess.run(
        ["pip", "freeze"],
        capture_output=True,
        text=True,
        check=True
    )
    print(result.stdout)

    with open("requirements.txt", "w") as f:
        f.write(result.stdout)


def main():
    check_env()
    install_libraries()
    show_installed()


if __name__ == "__main__":
    main()
