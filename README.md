# Python CLI Task Manager

A lightweight terminal application for keeping track of pending logistics
operations tasks. Tasks can be added, listed, deleted, and saved to or loaded
from a local CSV file.

## Requirements

- Python 3
- No third-party packages; the application uses only the Python standard
	library.

## Run the application

From the project directory, run:

```bash
python main.py
```

On systems where Python 3 is invoked with `python3`, use `python3 main.py`.

## Menu options

1. **Add a task** — enter a non-empty task title. It is appended to the current
	 list.
2. **View all tasks** — display tasks in order, numbered from 1.
3. **Delete a task** — enter the displayed number of the task to remove.
4. **Save tasks** — overwrite the saved CSV file with the current list.
5. **Load tasks** — replace the current list with tasks from the saved file.
6. **Exit** — close the application.

The menu repeats until Exit is selected. Changes are held in memory until you
choose Save; exiting does not save automatically.

## CSV storage

The application reads and writes `todos.csv` in the current working directory.
Saving overwrites the existing file and writes one task title per CSV row in
list order. Loading replaces the in-memory list (it does not append duplicates).
If the file is missing, loading clears the list and displays a friendly message.
An empty file loads as an empty list. File read and write failures are reported
without terminating the menu.

## Example terminal usage

```text
Task Manager
1. Add a task
2. View all tasks
3. Delete a task
4. Save tasks
5. Load tasks
6. Exit
Choose an option (1-6): 1
Enter the task title: Confirm delivery window
Task added: "Confirm delivery window"
Choose an option (1-6): 2
Pending tasks:
1. Confirm delivery window
Choose an option (1-6): 4
Saved 1 task(s) to todos.csv.
```

## Testing

Run the built-in Python syntax check with:

```bash
python -m py_compile main.py
```

There is no external test dependency. The required flows can be checked
interactively: add multiple tasks, view and delete by displayed number, save,
exit, restart, and load. Also try blank task titles, invalid menu choices,
non-numeric and out-of-range task numbers, deleting from an empty list, and
loading when `todos.csv` is missing or empty. The operations handle these cases
with messages rather than unexpected termination.
