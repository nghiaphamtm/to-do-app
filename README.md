### Project Description: Command-Line To-Do List Application

This project is a simple **command-line To-Do List application** written in Python. It demonstrates how to organize a program into multiple files, with each file responsible for a specific part of the application. The program allows users to create, manage, and save their personal tasks through an interactive text-based menu.

#### Features

* View all tasks along with their completion status.
* Add new tasks to the list.
* Mark tasks as completed.
* Automatically save tasks to a file so they persist between sessions.
* Load previously saved tasks when the program starts.

#### Project Structure

* **`main.py`** – The entry point of the application. It displays the menu, handles user input, and coordinates program execution.
* **`todo.py`** – Contains the `TodoList` class, which manages task operations such as adding, completing, displaying, loading, and saving tasks.
* **`storage.py`** – Handles reading from and writing to the data file using JSON, keeping file operations separate from the application logic.
* **`utils.py`** – Provides helper functions, such as formatting tasks for display.
* **`tasks.txt`** – Stores the task data in JSON format, allowing tasks to be preserved between program runs.

#### Learning Objectives

This project helps beginners understand:

* How to split a Python project into multiple modules.
* Object-oriented programming using classes.
* Reading and writing JSON files.
* Importing functions and classes from other files.
* Separating user interface, business logic, and data storage for cleaner, more maintainable code.

#### Possible Future Enhancements

* Delete tasks.
* Edit existing tasks.
* Add due dates and priorities.
* Search or filter tasks.
* Sort tasks by completion status or due date.
* Create a graphical user interface (GUI) using Tkinter or PyQt.
* Store tasks in a database such as SQLite instead of a text file.

This project is an excellent beginner-to-intermediate example of building a modular Python application while following good software design practices.
