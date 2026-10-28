# Technical Learning Report
## Topic: Command-Line Interface (CLI) and Python Fundamentals
## Date: 27 October 2026
## Tools Used: Windows Command Prompt (CMD), Python 3.13, VS Code, pyreadline3
## 1. Objective
The objective was to become comfortable using the command line, understand how to run Python programs, and practise basic Python programming through a simple task-list application. I also started learning how to create, read, and write files using Python.
## 2. Work Done
-	Practised navigating directories and managing folders using CMD.
-	Used commands such as cd, dir, mkdir, and cls.
-	Learned to create, rename, read, and write files using CMD.
-	Ran Python commands directly from the terminal using python and python -c.
-	Explored Python's interactive mode and installed pyreadline3 while investigating command-line input and history behaviour.
-	Built a menu-driven Todoist application in Python.
-	Implemented adding, viewing, updating, and deleting tasks.
-	Used terminal colour codes to make the menu easier to read.
-	Started learning Python file handling using open(), read(), write(), and different file modes.
## 3. Concepts Learned
-	CLI: A way to interact with a computer by entering commands instead of using graphical controls.
-	Directories and paths: How to navigate between folders and locate files.
-	Python interactive mode vs scripts: Interactive mode runs commands individually, while a .py file stores code that can be executed as a program.
-	Lists and indexing: Lists store multiple items, and Python uses zero-based indexing to access them.
-	Loops and conditions: for loops process items, while if statements allow the program to make decisions.
-	Functions: Functions group reusable instructions, such as displaying the Todoist menu.
-	enumerate(): Provides a counter alongside each item in a sequence.
-	F-strings: Allow variables and expressions to be inserted into formatted text.
-	File handling: Python can create and access files using open(), with modes such as "r" for reading, "w" for writing, and "a" for appending.
-	with statement: Helps manage opened files by closing them automatically after the block finishes.
## 4. Challenges Faced
-	Encountered an import error when trying to use readline on Windows.
-	Investigated command-line input and editing behaviour and installed pyreadline3.
-	Encountered quoting issues while running Python commands directly through CMD.
-	Had to understand the difference between Python list positions and task numbers displayed to the user.
-	Encountered a variable-naming issue while iterating through tasks.
-	Needed to understand the difference between creating a file, overwriting its contents, and appending new text.
## 5. Solutions & Key Takeaways
-	Used python -m pip install pyreadline3 to install the Windows-compatible readline-related package.
-	Learned to use different quotation marks when passing Python code through CMD, for example: python -c "print('Hello')".
-	Used enumerate(tasks, start=1) to display task numbers starting from 1.
-	Used number - 1 when converting a displayed task number into a Python list index.
-	Corrected variable names in loops to avoid overwriting the original task-list variable.
-	Learned that > overwrites file contents in CMD, while >> appends text.
-	Learned that Python's "w" mode overwrites existing contents, whereas "a" appends to a file.
The main takeaway is that understanding how commands, variables, loops, and files work makes it easier to build and troubleshoot small programs independently.
## 6. Quick Notes
Useful CMD Commands

| Command | Purpose |
|---|---|
| `cd folder` | Enter a folder |
| `cd ..` | Move to the parent folder |
| `dir` | List files and folders |
| `mkdir folder` | Create a folder |
| `cls` | Clear the terminal |
| `ren old.txt new.txt` | Rename a file |
| `type notes.txt` | Display a text file |
| `type nul > notes.txt` | Create an empty file |
| `echo Hello > notes.txt` | Write text, replacing existing contents |
| `echo Hello >> notes.txt` | Append text to a file |t	Append text


# Useful Python Syntax
 # Create or overwrite a file
with open("notes.txt", "w") as file:
    file.write("Hello from Python")

# Read a file
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

# Append text
with open("notes.txt", "a") as file:
    file.write("\nAnother line")
Remember: "r" = read, "w" = write/overwrite, "a" = append, and "x" = create a new file without overwriting an existing one.
# 7. Current Status
## Completed and tested:
-	Basic CMD navigation and folder operations.
-	Basic file creation and text reading/writing through CMD.
-	Running Python commands from the terminal.
-	Core Todoist features: adding, viewing, updating, and deleting tasks.
-	Basic Python concepts used in the Todoist application.
## Currently learning or requiring further practice:
-	Creating, reading, and writing files independently in Python.
-	Handling invalid user input and unexpected errors reliably.
-	Understanding how to preserve data between program runs.
-	Using CLI commands confidently without relying on step-by-step instructions.

The Todoist application currently stores tasks in memory, so tasks do not persist after the program exits.
# 8. Next Steps
1.	Practise Python file handling by creating a file, writing text, reading it, and appending new text.
2.	Rebuild the Todoist application from scratch without copying the original code.
3.	Practise handling invalid input using try and except.
4.	Learn how to save tasks to a file and load them when the program starts.
5.	Exploring Django and FastAPI

