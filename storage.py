import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump([], f)
    with open(FILE_NAME, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # TODO: Handle the case where the file is empty or corrupted
            return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)
