import os

FILE_NAME = "tasks.txt"

def load_tasks():
    """Load tasks from file."""
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_id, title, status, description = line.strip().split("||")
                tasks.append({
                    "id": int(task_id),
                    "title": title,
                    "status": status,
                    "description": description
                })
    return tasks

def save_tasks(tasks):
    """Save tasks to file."""
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(f"{task['id']}||{task['title']}||{task['status']}||{task['description']}\n")

def add_task(tasks):
    """Add a new task."""
    task_id = len(tasks) + 1
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    tasks.append({
        "id": task_id,
        "title": title,
        "status": "Pending",
        "description": description
    })
    print("Task added successfully!")
    save_tasks(tasks)

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks available.")
        return
    print("\nAll Tasks:")
    print("{:<5} {:<20} {:<10} {:<30}".format("ID", "Title", "Status", "Description"))
    print("-" * 70)
    for task in tasks:
        print("{:<5} {:<20} {:<10} {:<30}".format(task["id"], task["title"], task["status"], task["description"]))
    print("-" * 70)

def update_task(tasks):
    """Update an existing task."""
    if not tasks:
        print("No tasks available to update.")
        return
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to update: ").strip())
        for task in tasks:
            if task["id"] == task_id:
                print(f"Selected Task: {task['title']} (Status: {task['status']})")
                new_status = input("Enter new status (Pending/Completed): ").strip()
                if new_status.lower() in ["pending", "completed"]:
                    task["status"] = new_status.capitalize()
                    print("Task updated successfully!")
                    save_tasks(tasks)
                else:
                    print("Invalid status. Please enter 'Pending' or 'Completed'.")
                return
        print("Task ID not found.")
    except ValueError:
        print("Invalid input. Please enter a valid task ID.")

def delete_task(tasks):
    """Delete a task."""
    if not tasks:
        print("No tasks available to delete.")
        return
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to delete: ").strip())
        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                deleted_task = tasks.pop(i)
                print(f"Deleted Task: {deleted_task['title']}")
                save_tasks(tasks)
                return
        print("Task ID not found.")
    except ValueError:
        print("Invalid input. Please enter a valid task ID.")

def search_tasks(tasks):
    """Search for tasks by title."""
    if not tasks:
        print("No tasks available to search.")
        return
    query = input("Enter keyword to search for: ").strip().lower()
    results = [task for task in tasks if query in task["title"].lower()]
    if results:
        print("\nSearch Results:")
        print("{:<5} {:<20} {:<10} {:<30}".format("ID", "Title", "Status", "Description"))
        print("-" * 70)
        for task in results:
            print("{:<5} {:<20} {:<10} {:<30}".format(task["id"], task["title"], task["status"], task["description"]))
        print("-" * 70)
    else:
        print("No tasks found with the given keyword.")

def main():
    """Main program loop."""
    tasks = load_tasks()
    while True:
        print("\nTask Management System")
        print("[1] Add Task")
        print("[2] View Tasks")
        print("[3] Update Task")
        print("[4] Delete Task")
        print("[5] Search Tasks")
        print("[6] Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            search_tasks(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select from the menu.")

if __name__ == "__main__":
    main()
