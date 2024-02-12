import json
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(description, priority, due_date):
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)

# Remove a task by id
def remove_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)

# Mark a task as completed
def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            break
    save_tasks(tasks)

# Display all tasks
def display_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("ID | Description             | Priority | Due Date   | Completed")
        print("-" * 65)
        for task in tasks:
            print(f"{task['id']:2} | {task['description']:23} | {task['priority']:8} | {task['due_date']:10} | {'Yes' if task['completed'] else 'No'}")

# Main function
def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority (HIGH/MEDIUM/LOW): ").upper()
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(description, priority, due_date)
        elif choice == "2":
            task_id = int(input("Enter task ID to remove: "))
            remove_task(task_id)
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as completed: "))
            complete_task(task_id)
        elif choice == "4":
            display_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()