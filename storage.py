import json
import os

FILE_NAME = "tasks.json"
ARCHIVE_FILE = "archive.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump([], f)
    with open(FILE_NAME, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error: {e}")
            return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)


def load_archived_tasks():
    if not os.path.exists(ARCHIVE_FILE):
        with open(ARCHIVE_FILE, "w") as f:
            json.dump([], f)
    with open(ARCHIVE_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error: {e}")
            return []


def save_archived_tasks(tasks):
    with open(ARCHIVE_FILE, "w") as f:
        json.dump(tasks, f, indent=4)
