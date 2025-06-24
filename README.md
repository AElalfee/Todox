
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

- **Clone the repository**:

```bash
  git clone https://github.com/AElalfee/Todox.git
  
  cd todox
```

- **Install depenedencies**

```bash
pip install -r requirements.txt 
```

- **Create virtual environment**

```bash
python3 -m venv .venv
```


- **Activate virtual environment**

```bash
source .venv/Scripts/activate
```

- **Make the file executable**:

```bash
chmod +x todox
```

- **Move it to a location in your `PATH`** (e.g., /usr/local/bin):

```bash
sudo mv todox /usr/local/bin/
```

## Usage/Examples

- **Add task**:

```bash
todox add -d "First task"

╭──────┬───────────────┬──────────┬─────────────────────────┬─────────────────────────╮
│   id │ description   │ status   │ created_at              │ updated_at              │
├──────┼───────────────┼──────────┼─────────────────────────┼─────────────────────────┤
│    1 │ First task    │ todo     │ 24 Jun 2025 at 13:22:46 │ 24 Jun 2025 at 13:22:46 │
╰──────┴───────────────┴──────────┴─────────────────────────┴─────────────────────────╯

```

- **List tasks**:

```bash
todox list

╭──────┬───────────────┬──────────┬─────────────────────────┬─────────────────────────╮
│   id │ description   │ status   │ created_at              │ updated_at              │
├──────┼───────────────┼──────────┼─────────────────────────┼─────────────────────────┤
│    1 │ First task    │ todo     │ 24 Jun 2025 at 13:22:46 │ 24 Jun 2025 at 13:22:46 │
╰──────┴───────────────┴──────────┴─────────────────────────┴─────────────────────────╯

```

- **Get task by id**:

```bash
todox get -i 1

╭──────┬───────────────┬──────────┬─────────────────────────┬─────────────────────────╮
│   id │ description   │ status   │ created_at              │ updated_at              │
├──────┼───────────────┼──────────┼─────────────────────────┼─────────────────────────┤
│    1 │ First task    │ todo     │ 24 Jun 2025 at 13:22:46 │ 24 Jun 2025 at 13:22:46 │
╰──────┴───────────────┴──────────┴─────────────────────────┴─────────────────────────╯

```

- **Update task**:

```bash
todox update -i 1 -d "Write code"

╭──────┬───────────────┬──────────┬─────────────────────────┬─────────────────────────╮
│   id │ description   │ status   │ created_at              │ updated_at              │
├──────┼───────────────┼──────────┼─────────────────────────┼─────────────────────────┤
│    1 │ Write code    │ todo     │ 24 Jun 2025 at 13:22:46 │ 24 Jun 2025 at 13:23:48 │
╰──────┴───────────────┴──────────┴─────────────────────────┴─────────────────────────╯

```

- **Update task Status**:

```bash
todox status -i 1 -s in_progress

╭──────┬───────────────┬─────────────┬─────────────────────────┬─────────────────────────╮
│   id │ description   │ status      │ created_at              │ updated_at              │
├──────┼───────────────┼─────────────┼─────────────────────────┼─────────────────────────┤
│    1 │ Write code    │ in_progress │ 24 Jun 2025 at 13:22:46 │ 24 Jun 2025 at 13:24:20 │
╰──────┴───────────────┴─────────────┴─────────────────────────┴─────────────────────────╯

```

- **Delete task**:

```bash
todox delete -i 1
```

- **List tasks by status**:

```bash
todox list -s in_progress

╭──────┬───────────────┬─────────────┬─────────────────────────┬─────────────────────────╮
│   id │ description   │ status      │ created_at              │ updated_at              │
├──────┼───────────────┼─────────────┼─────────────────────────┼─────────────────────────┤
│    1 │ Write code    │ in_progress │ 24 Jun 2025 at 13:22:46 │ 24 Jun 2025 at 13:24:20 │
╰──────┴───────────────┴─────────────┴─────────────────────────┴─────────────────────────╯

```