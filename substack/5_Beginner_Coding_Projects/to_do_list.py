def display_tasks(tasks):
    if not tasks:
        print("\nYour To-Do List is empty.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Added task: {task}")
    else:
        print("Task cannot be empty.")

def remove_task(tasks):
    display_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 0 < task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Removed task: {removed_task}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

def main():
    tasks = []
    while True:
        choice = input("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Quit\nChoose an option: ").strip()
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            display_tasks(tasks)
        elif choice == '4':
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

main()
