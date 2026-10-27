GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

tasks = []

def show_menu():
    print(f"\n{CYAN} TODOIST{RESET}")
    print(f"{GREEN}1. Add a Task{RESET}")
    print(f"{CYAN}2. View Task{RESET}")
    print(f"{YELLOW}3. Update a Task{RESET}")
    print(f"{RED}4 . Delete a Task{RESET}")
    print(f"{YELLOW}5 .Exit{RESET}")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ").strip()

    if choice =="1":
        task = input("Enter your task: ").strip()
        if task:
            tasks.append(task)
            print("Task added!")
        else:
            print("Task cannot be empty.")

    elif choice == "2":
        if not tasks:
            print("No tasks found ")
        else:
             for index, task in enumerate(tasks,start=1):
                 print(f"{index}. {task}") 
    elif choice == "3":
        if not tasks:
            print("No tasks to update.")
        else:
            for index , task in enumerate(tasks, start=1):
                print(f"{index}.{task}")
            try:
                number = int(input("Enter the task number to be updated: ").strip())
            except:
                print("Please enter a valid input")
                continue
            if 1 <= number <=len(tasks):
                new_task = input("New Task: ").strip()

                if new_task:
                    print(tasks)
                    print(type(tasks))
                    tasks[number - 1] = new_task
                    print("Task Updated!")
                else:
                    print("Tasks cannot be empty")
            else:
                print("Invalid task number")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            for index,task in enumerate(tasks,start=1):
                print(f"{index}. {task}")

                try:
                    number = int(input("Enter task number to delete: "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue

            if 1<= number <=len(tasks):
                deleted_Task = tasks.pop(number -1)
                print("Deleted:" , deleted_Task)
            else:
                print("Invalid Task number.")
    elif choice == "5":
        print("Goodbye")
        break