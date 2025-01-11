import json
from datetime import datetime

# File to store tasks
tasks_file = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    try:
        with open(tasks_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(tasks_file, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    """Add a new task."""
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (Low/Medium/High): ")

    try:
        if due_date:
            datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Task not added.\n")
        return

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "status": "Pending"
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks found.\n")
        return

    print("\n--- To-Do List ---")
    for task in tasks:
        print(f"ID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Due Date: {task['due_date']}")
        print(f"Priority: {task['priority']}")
        print(f"Status: {task['status']}\n")

def update_task(tasks):
    """Update an existing task."""
    try:
        task_id = int(input("Enter task ID to update: "))
    except ValueError:
        print("Invalid ID. Please enter a numeric value.\n")
        return

    for task in tasks:
        if task['id'] == task_id:
            task['title'] = input(f"Enter new title ({task['title']}): ") or task['title']
            task['description'] = input(f"Enter new description ({task['description']}): ") or task['description']
            new_due_date = input(f"Enter new due date ({task['due_date']}): ")
            if new_due_date:
                try:
                    datetime.strptime(new_due_date, "%Y-%m-%d")
                    task['due_date'] = new_due_date
                except ValueError:
                    print("Invalid date format. Due date not updated.")
            task['priority'] = input(f"Enter new priority ({task['priority']}): ") or task['priority']
            task['status'] = input(f"Enter new status (Pending/Completed) ({task['status']}): ") or task['status']
            save_tasks(tasks)
            print("Task updated successfully!\n")
            return
    print("Task not found.\n")

def delete_task(tasks):
    """Delete a task."""
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a numeric value.\n")
        return

    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully!\n")
            return
    print("Task not found.\n")

def main():
    """Main function to run the To-Do List application."""
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
