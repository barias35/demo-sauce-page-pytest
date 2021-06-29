import os
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def get_screenshots_dir():
    dir_name = f"{get_project_root().parent}\\screenshots"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        print("Directory ", dir_name, " Created ")
    else:
        print("Directory ", dir_name, " already exists")
    return
