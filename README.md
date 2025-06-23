
# Todox

A lightweight command-line TODO application written in Python that stores your tasks in a local JSON file.  
Easily add, update, delete, and manage tasks with clear statuses: `todo`, `in_progress`, and `done`.

<a href="https://roadmap.sh/projects/task-tracker" target="_blank">
<img src="todox.gif" alt="Preview">
</a>


## Features

- Add new tasks with descriptions
- Update task descriptions
- Delete tasks by ID
- Change task statuses
- List all tasks or filter by status
- Tasks are saved to a local `tasks.json` file
- No external dependencies — built entirely with Python standard libraries


## Project Structure

- **main.py**: main file (CLI Entrypoint) 
- **task_manager.py**: Contains core functions
- **storage.py**: Handles JSON loading & saving
- **utils.py**: Contains helper functions.
- **tests.py**: Contains tests for core functions
## Installation

Make sure you have Python 3 installed.

1- **Clone the repository**:

```bash
  git clone https://github.com/AElalfee/Todox.git
  cd todox
```

2- **Make the file executable**:

```bash
chmod +x todox
```

3- **Move it to a location in your `PATH`** (e.g., /usr/local/bin):

```bash
sudo mv todox /usr/local/bin/
```

## Usage/Examples

- **Add task**:

```bash
todox add -d "First task"
```

- **List tasks**:

```bash
todox list

[{'id': 1, 'description': 'First task', 'status': 'todo', 'created_at': '2025-06-23T15:59:39.889091', 'updated_at': '2025-06-23T15:59:39.889117'}]
```

- **Get task by id**:

```bash
todox get -i 1

[{'id': 1, 'description': 'First task', 'status': 'todo', 'created_at': '2025-06-23T15:59:39.889091', 'updated_at': '2025-06-23T15:59:39.889117'}]
```

- **Update task**:

```bash
todox update -i 1 -d "Write code"
```

- **Update task Status**:

```bash
todox status -i 1 -s in_progress
```

- **Delete task**:

```bash
todox delete -i 1
```

- **List tasks by status**:

```bash
todox list -s in_progress

[{'id': 1, 'description': 'Write code', 'status': 'in_progress', 'created_at': '2025-06-23T15:59:39.889091', 'updated_at': '2025-06-23T16:05:32.964807'}]
```