from storage import load_tasks, save_tasks
from utils import now_iso

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
        except ValueError:
            pass
    task = {
        "id": next_id,
        "description": description,
        "status": status,
        "created_at": now_iso(),
        "updated_at": now_iso(),
    }
    tasks.append(task)
    save_tasks(tasks)


def get_task_by_id(id: int):
    tasks = load_tasks()
    return [task for task in tasks if task["id"] == id]


def get_tasks(status: str = None):
    tasks = load_tasks()
    if status:
        if status not in STATUS_OPTIONS:
            return
        return [task for task in tasks if task["status"] == status]
    return tasks


def update_task(id: int, description: str):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            task["description"] = description
            task["updated_at"] = now_iso()
            save_tasks(tasks)
            return


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
            return


def delete_task(id: int):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != id]
    save_tasks(tasks)
