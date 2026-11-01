import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    with DATA_FILE.open("w") as file:
        json.dump(tasks, file, indent=2)


def add_task():
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return

    tasks = load_tasks()
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print(f"Task '{title}' added successfully.")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task.get("completed") else "Pending"
        print(f"{index}. {task['title']} - {status}")


def mark_completed():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to update.")
        return

    list_tasks()
    try:
        choice = int(input("Enter task number to mark as completed: ")) - 1
    except ValueError:
        print("Invalid task number.")
        return

    if 0 <= choice < len(tasks):
        tasks[choice]["completed"] = True
        save_tasks(tasks)
        print(f"Task '{tasks[choice]['title']}' marked as completed.")
    else:
        print("Task number out of range.")


def delete_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to delete.")
        return

    list_tasks()
    try:
        choice = int(input("Enter task number to delete: ")) - 1
    except ValueError:
        print("Invalid task number.")
        return

    if 0 <= choice < len(tasks):
        removed = tasks.pop(choice)
        save_tasks(tasks)
        print(f"Task '{removed['title']}' deleted.")
    else:
        print("Task number out of range.")


def show_menu():
    print("\nTask Manager")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
