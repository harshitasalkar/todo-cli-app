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


def clear_tasks():
    with open("tasks.txt", "w") as f:
        f.write("")
    print("All tasks cleared!")


# Main program
while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Clear all tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        clear_tasks()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
