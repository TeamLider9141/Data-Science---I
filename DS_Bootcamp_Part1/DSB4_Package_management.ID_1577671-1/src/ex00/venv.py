#!/usr/bin/env python3
import os


def show_env():
    env_path = os.environ.get("VIRTUAL_ENV")
    if not env_path:
        raise Exception("No virtual environment is active")
    print(f"Your current virtual env is {env_path}")


if __name__ == "__main__":
    show_env()


#executuable => qilish esdan chiqmasina => chmod +x venv.py

#active qilish =>source eaduinte/bin/activate

# ishga tushirish ./venv.py

#deactivate qilish uchun =>
# deactivate
#./venv.py
# => diactivae vaqtidagi natija => Expection bilan chiqadi
