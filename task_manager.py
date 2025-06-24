from tabulate import tabulate

from storage import load_tasks, save_tasks
from utils import date_format, now_iso

STATUS_OPTIONS = ["todo", "in_progress", "done"]


def add_task(description: str, status: str = "todo"):
    next_id = 1
    if status not in STATUS_OPTIONS:
        print(
            f"Error: {status} is not in the following options [todo, in_progress, done]."
        )
        return
    tasks = load_tasks()
    if tasks:
        try:
            next_id = max(task["id"] for task in tasks) + 1
        except ValueError as e:
            print(f"Error: {e}")
            return
    task = {
        "id": next_id,
        "description": description,
        "status": status,
        "created_at": now_iso(),
        "updated_at": now_iso(),
    }
    tasks.append(task)
    save_tasks(tasks)
    task["created_at"] = date_format(task["created_at"])
    task["updated_at"] = date_format(task["updated_at"])
    print(tabulate([task], headers="keys", tablefmt="rounded_outline"))


def get_task_by_id(id: int):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            task["created_at"] = date_format(task["created_at"])
            task["updated_at"] = date_format(task["updated_at"])
            print(tabulate([task], headers="keys", tablefmt="rounded_outline"))
            return
    print(f"No task found with this ID: {id}")


def get_tasks(status: str = None):
    tasks = load_tasks()
    if status:
        if status not in STATUS_OPTIONS:
            print(
                f"Error: {status} is not in the following options [todo, in_progress, done]."
            )
            return
        tasks = [task for task in tasks if task["status"] == status]

    for task in tasks:
        task["created_at"] = date_format(task["created_at"])
        task["updated_at"] = date_format(task["updated_at"])
    print(tabulate(tasks, headers="keys", tablefmt="rounded_outline"))


def update_task(id: int, description: str):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            task["description"] = description
            task["updated_at"] = now_iso()
            save_tasks(tasks)
            task["created_at"] = date_format(task["created_at"])
            task["updated_at"] = date_format(task["updated_at"])
            print(tabulate([task], headers="keys", tablefmt="rounded_outline"))
            return
    print(f"No task found with this ID: {id}")


def update_task_status(id: int, status: str):
    if status not in STATUS_OPTIONS:
        print(
            f"Error: {status} is not in the following options [todo, in_progress, done]."
        )
        return
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            task["status"] = status
            task["updated_at"] = now_iso()
            save_tasks(tasks)
            task["created_at"] = date_format(task["created_at"])
            task["updated_at"] = date_format(task["updated_at"])
            print(tabulate([task], headers="keys", tablefmt="rounded_outline"))
            return
    print(f"No task found with this ID: {id}")


def delete_task(id: int):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != id]
    save_tasks(tasks)
