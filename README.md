# PyTaskManager 📝

A simple CLI-based task manager written in Python. Manage multiple task lists, add, update, and remove tasks with ease—all from your terminal.

## 🚀 Features

- Create and manage multiple task lists
- Add, update, and delete tasks
- Task statuses: done or not done
- View all task lists or list specific tasks
- Persistent storage using JSON
- Command-line interface with color-coded output

## 🛠 Installation

```bash
git clone https://github.com/N0r3b0/PyTaskManager.git
cd PyTaskManager
pip install -r requirements.txt
```

## 📦 Usage

```bash
python main.py [options]
```

### Common Commands

- `-c <name>` – Create a new task list
- `-l <name>` – Specify a task list
- `-a <name> <description> <status>` – Add a task
- `-d <id>` – Delete a task by ID
- `-s` – Show task lists or tasks from selected list
- `update -l <list> --id <id> [--name NAME] [--desc DESC] [--status STATUS]` – Update a task
- `--clear` – Clear all or selected task list
- `-v` – Show version info

Example:
```bash
python main.py -c mylist
python main.py -l mylist -a "Buy milk" "Almond preferred" "done"
python main.py -l mylist -s
```

## ✅ Status Values

Use one of the following for a "done" task:
- `true`, `yes`, `1`, `done`

## 📁 Data Storage

All task data is stored in the `data/` folder as JSON files.

## 🧑‍💻 Author

[**N0r3b0**](https://github.com/N0r3b0)