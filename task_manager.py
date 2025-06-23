from datetime import datetime

from storage import load_tasks, save_tasks

STATUS_OPTIONS = ["todo", "in_progress", "done"]


def add_task(description: str, status: str = "todo"):
    next_id = 1
    if status not in STATUS_OPTIONS:
        # TODO: Handle invalid status
        return
    tasks = load_tasks()
    if tasks:
        try:
            next_id = max(task["id"] for task in tasks) + 1
        except ValueError:
            pass
    now = datetime.now().isoformat()
    task = {
        "id": next_id,
        "description": description,
        "status": status,
        "created_at": now,
        "updated_at": now,
    }
    tasks.append(task)
    save_tasks(tasks)


def get_task_by_id(id: int):
    tasks = load_tasks()
    return [task for task in tasks if task["id"] == id]


def get_tasks(status: str = None):
    if status not in STATUS_OPTIONS:
        # TODO: Handle invalid status
        return
    tasks = load_tasks()
    if status:
        return [task for task in tasks if task["status"] == status]
    return tasks


def update_task(id: int, description: str):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            task["description"] = description
            task["updated_at"] = datetime.now().isoformat()
            save_tasks(tasks)
            return


def update_task_status(id: int, status: str):
    if status not in STATUS_OPTIONS:
        # TODO: Handle invalid status
        return
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            task["status"] = status
            task["updated_at"] = datetime.now().isoformat()
            save_tasks(tasks)
            return


def delete_task(id: int):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != id]
    save_tasks(tasks)
