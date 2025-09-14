# Todo-application
To-Do List Application

A simple console-based to-do list manager with persistent storage.

Features

· Add Tasks: Add new tasks to your to-do list
· Remove Tasks: Remove tasks by their index number
· View Tasks: Display all current tasks with numbering
· Persistence: Tasks are automatically saved to a text file and reloaded on startup

How to Use

1. Run the application:
   ```
   python todo.py
   ```
2. Use the menu options:
   · Press 1 to add a new task
   · Press 2 to remove an existing task
   · Press 3 to view all tasks
   · Press 4 to exit the application
3. Tasks are automatically saved to todo.txt in the same directory

File Storage

The application stores tasks in a simple text file (todo.txt) with each task on a separate line. The file is created automatically if it doesn't exist.

Requirements

· Python 3.x
· No external dependencies

Code Structure

The application uses:

· File handling with open() and context managers (with statement)
· Lists to store and manage tasks
· String manipulation for processing user input
· Error handling for file operations

The code is organized into functions for loading tasks, saving tasks, adding tasks, removing tasks, and viewing tasks, with a main function that handles the user interface.
