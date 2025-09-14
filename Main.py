# todo.py
import os

TODO_FILE = "todo.txt"

def load_tasks():
    """Load tasks from the text file if it exists."""
    tasks = []
    if os.path.exists(TODO_FILE):
        try:
            with open(TODO_FILE, 'r') as file:
                for line in file:
                    task = line.strip()
                    if task:  # Only add non-empty lines
                        tasks.append(task)
        except IOError:
            print("Error: Could not read from file.")
    return tasks

def save_tasks(tasks):
    """Save tasks to the text file."""
    try:
        with open(TODO_FILE, 'w') as file:
            for task in tasks:
                file.write(task + '\n')
    except IOError:
        print("Error: Could not write to file.")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{task}' added successfully.")
    else:
        print("Task cannot be empty.")

def remove_task(tasks):
    """Remove a task by its index."""
    if not tasks:
        print("No tasks to remove.")
        return
    
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks(tasks):
    """Display all tasks with their numbers."""
    if not tasks:
        print("No tasks in the list.")
        return
    
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

def main():
    """Main function to run the to-do list application."""
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
