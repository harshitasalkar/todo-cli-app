# todo.py

def add_task():
    while True:
        task = input("Enter task: ")

        with open("tasks.txt", "a") as f:
            f.write(task + "\n")

        stop = input("Stop entering task (y/n): ").lower()
        if stop == 'y':
            break


def show_task():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()

        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i].strip())

    except FileNotFoundError:
        print("No tasks file found. Add tasks first.")


def remove_task():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()

        if len(tasks) == 0:
            print("No tasks to remove.")
            return

        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i].strip())

        remove = int(input("Enter task number to remove: "))

        if remove < 1 or remove > len(tasks):
            print("Invalid task number.")
            return

        tasks.pop(remove - 1)

        with open("tasks.txt", "w") as f:
            f.writelines(tasks)

        print("Task removed successfully!")

    except FileNotFoundError:
        print("No tasks file found.")

def replace_task():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
        
        if len(tasks) == 0:
            print("No tasks to replace.")
            return

        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i].strip())
        while True:
            replace = int(input("Enter task number to replace:"))
            if replace<1 or replace>len(tasks):
                print("Invalid task number.")
                continue
            tasks[replace-1]=input("Enter new task:")+"\n"
            more=input("Do you want to replace more tasks(y/n):").lower()
            if more=="y":
                continue
            else:
                break
        
        with open("tasks.txt", "w") as f:
            f.writelines(tasks)
        print("Task replaced!")
    
    except FileNotFoundError:
        print("No tasks file found.")

def search_task():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
        
        if len(tasks) == 0:
            print("No tasks to replace.")
            return
        word=input("Enter word to search:")
        for i in range(len(tasks)):
            if word in tasks[i].lower():
                print(i + 1, ".", tasks[i])
                print("Word found!")   
        
        with open("tasks.txt", "w") as f:
            f.writelines(tasks)
    
    except FileNotFoundError:
        print("No tasks file found.")

        
def clear_tasks():
    with open("tasks.txt", "w") as f:
        f.write("")
    print("All tasks cleared!")


# Main program
while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Replace task")
    print("5. Search task")
    print("6. Clear all tasks")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        replace_task()
    elif choice=="5":
        search_task()
    elif choice=="6":
        clear_tasks()
    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")