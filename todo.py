import json
import os

TODO_FILE = 'todo.json'


def load_todo():
    """Load the todo list from a file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []


def save_todo(todo_list):
    """Save the todo list to a file."""
    with open(TODO_FILE, 'w') as file:
        json.dump(todo_list, file)


def add_task(task):
    """Add a new task to the todo list."""
    todo_list = load_todo()
    todo_list.append(task)
    save_todo(todo_list)
    print(f'Task added: "{task}"')


def view_tasks():
    """View all tasks in the todo list."""
    todo_list = load_todo()
    if not todo_list:
        print("Your todo list is empty.")
    else:
        print("Your todo list:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")


def delete_task(task_number):
    """Delete a task from the todo list by its number."""
    todo_list = load_todo()
    try:
        task_number = int(task_number) - 1
        if 0 <= task_number < len(todo_list):
            removed_task = todo_list.pop(task_number)
            save_todo(todo_list)
            print(f'Task removed: "{removed_task}"')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_number = input("Enter the task number to delete: ")
            delete_task(task_number)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == '__main__':
    main()
