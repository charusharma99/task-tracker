def show_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks found.")
        else:
            print("My Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")

    except FileNotFoundError:
        print("tasks.txt does not exist yet.")


def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

    print("Task added.")


print("1. Show tasks")
print("2. Add task")

choice = input("Choose an option: ")

if choice == "1":
    show_tasks()
elif choice == "2":
    new_task = input("Enter task: ")
    add_task(new_task)
else:
    print("Invalid choice")

def delete_task(task_number):
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
        return

    deleted_task = tasks.pop(task_number - 1)

    with open("tasks.txt", "w") as file:
        file.writelines(tasks)

    print(f"Deleted: {deleted_task.strip()}")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")