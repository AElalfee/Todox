import unittest

from task_manager import (
    add_task,
    get_tasks,
    update_task,
    delete_task,
    update_task_status,
)


class TestExample(unittest.TestCase):
    def setUp(self):
        self.description = "Test task"
        for task in get_tasks():
            delete_task(task["id"])
        self.task_id = None
        if self._testMethodName != "test_add_task":
            add_task(self.description)
            task = next(t for t in get_tasks() if t["description"] == self.description)
            self.task_id = task["id"]

    def tearDown(self):
        for task in get_tasks():
            delete_task(task["id"])

    def test_add_task(self):
        add_task(self.description)
        tasks = get_tasks()
        self.assertIn(self.description, [task["description"] for task in tasks])

    def test_update_task(self):
        update_task(self.task_id, "Updated task")
        tasks = get_tasks()
        self.assertIn("Updated task", [task["description"] for task in tasks])

    def test_update_task_status(self):
        update_task_status(self.task_id, "done")
        tasks = get_tasks()
        self.assertIn("done", [task["status"] for task in tasks])

    def test_delete_task(self):
        delete_task(self.task_id)
        tasks = get_tasks()
        self.assertNotIn(self.description, [task["description"] for task in tasks])
