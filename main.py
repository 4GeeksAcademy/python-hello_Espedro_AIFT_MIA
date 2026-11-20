"""A small command-line task manager backed by a CSV file."""

import csv


TODO_FILE = "todos.csv"
todos = []


def add_one_task(title):
	"""Add a non-empty task title to the active task list."""
	clean_title = title.strip()
	if not clean_title:
		print("Task title cannot be empty.")
		return False

	todos.append(clean_title)
	print(f'Task added: "{clean_title}"')
	return True


def print_list():
	"""Display active tasks in their current order."""
	if not todos:
		print("Your task list is empty.")
		return

	print("Pending tasks:")
	for position, title in enumerate(todos, start=1):
		print(f"{position}. {title}")


def delete_task(number_to_delete):
	"""Delete a task using its displayed, one-based position."""
	if not todos:
		print("There are no tasks to delete.")
		return False

	try:
		position = int(number_to_delete)
	except (TypeError, ValueError):
		print("Please enter a valid numeric task position.")
		return False

	if position < 1 or position > len(todos):
		print(f"Choose a task number from 1 to {len(todos)}.")
		return False

	removed_title = todos.pop(position - 1)
	print(f'Task deleted: "{removed_title}"')
	return True


def save_todos():
	"""Overwrite todos.csv with the active tasks, in order."""
	try:
		with open(TODO_FILE, "w", newline="", encoding="utf-8") as csv_file:
			writer = csv.writer(csv_file)
			for title in todos:
				writer.writerow([title])
	except (OSError, csv.Error) as error:
		print(f"Could not save tasks: {error}")
		return False

	print(f"Saved {len(todos)} task(s) to {TODO_FILE}.")
	return True


def load_todos():
	"""Replace active tasks with the tasks saved in todos.csv."""
	loaded_tasks = []
	try:
		with open(TODO_FILE, "r", newline="", encoding="utf-8") as csv_file:
			reader = csv.reader(csv_file)
			for row in reader:
				if row:
					loaded_tasks.append(row[0])
	except FileNotFoundError:
		todos.clear()
		print(f"No saved task file found ({TODO_FILE}); the task list is empty.")
		return False
	except (OSError, csv.Error, UnicodeError) as error:
		print(f"Could not load tasks: {error}")
		return False

	todos[:] = loaded_tasks
	print(f"Loaded {len(todos)} task(s) from {TODO_FILE}.")
	return True


def print_menu():
	"""Display the available task manager actions."""
	print("\nTask Manager")
	print("1. Add a task")
	print("2. View all tasks")
	print("3. Delete a task")
	print("4. Save tasks")
	print("5. Load tasks")
	print("6. Exit")


def main():
	"""Run the interactive task manager menu until the user exits."""
	while True:
		print_menu()
		choice = input("Choose an option (1-6): ").strip()

		if choice == "1":
			title = input("Enter the task title: ")
			add_one_task(title)
		elif choice == "2":
			print_list()
		elif choice == "3":
			if todos:
				print_list()
				position = input("Enter the task number to delete: ")
				delete_task(position)
			else:
				print("There are no tasks to delete.")
		elif choice == "4":
			save_todos()
		elif choice == "5":
			load_todos()
		elif choice == "6":
			print("Goodbye!")
			break
		else:
			print("Invalid menu choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
	main()