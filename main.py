import argparse

from task_manager import (
    add_task,
    delete_task,
    get_task_by_id,
    get_tasks,
    update_task,
    update_task_status,
    archive_done_tasks,
    get_archived_tasks,
)


def main():
    parser = argparse.ArgumentParser(
        prog="Todox",
        usage="%(prog)s [options]",
        epilog="For more information, visit https://github.com/AElalfee/Todox",
        description="A simple CLI todo manager.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument(
        "-d", "--description", type=str, help="Task description", required=True
    )
    parser_add.add_argument(
        "-s",
        "--status",
        type=str,
        help="Task status",
        choices=["todo", "in_progress", "done"],
        default="todo",
        nargs="?",
    )

    parser_update = subparsers.add_parser("update", help="Update an existing task")
    parser_update.add_argument("-i", "--id", type=int, help="Task ID", required=True)
    parser_update.add_argument(
        "-d", "--description", type=str, help="New task description", required=True
    )

    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("-i", "--id", type=int, help="Task ID", required=True)

    parser_status = subparsers.add_parser("status", help="Update task status")
    parser_status.add_argument("-i", "--id", type=int, help="Task ID", required=True)
    parser_status.add_argument(
        "-s",
        "--status",
        type=str,
        help="New task status",
        choices=["todo", "in_progress", "done"],
        required=True,
    )

    parser_get = subparsers.add_parser("get", help="Get a task by ID")
    parser_get.add_argument("-i", "--id", type=int, help="Task ID", required=True)

    parser_list = subparsers.add_parser("list", help="List all tasks")
    parser_list.add_argument(
        "-s",
        "--status",
        type=str,
        help="Filter tasks by status",
        choices=["todo", "in_progress", "done"],
        nargs="?",
    )
    parser_list.add_argument(
        "--archive",
        action="store_true",
        help="List all archived tasks.",
    )

    subparsers.add_parser("archive", help="Archive all done tasks")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description, args.status)
    elif args.command == "update":
        update_task(args.id, args.description)
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "status":
        update_task_status(args.id, args.status)
    elif args.command == "get":
        get_task_by_id(args.id)
    elif args.command == "list":
        if args.archive:
            get_archived_tasks()
        else:
            get_tasks(args.status if hasattr(args, "status") else None)
    elif args.command == "archive":
        archive_done_tasks()


if __name__ == "__main__":
    main()
