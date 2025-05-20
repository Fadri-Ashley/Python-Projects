todo_list = []

def show_menu():
    print("\n=== TO-DO LIST ===")
    print("1. Show All Tasks")
    print("2. Add a Task")
    print("3. Delete Task")
    print("4. Out")

def show_task():
    if not todo_list:
        print("There is no task yet.")
    else:
        print("\nTasks: ")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}.{task}")

def add_task():
    task = input("Add task: ")
    todo_list.append(task)
    print("Task Add Successfully!")

def delete_task():
    show_task()
    try:
        index = int(input("Input task number for delete it: "))
        if 1 <= index <= len(todo_list):
            task = todo_list.pop(index - 1)
            print(f"Task '{task}' deleted")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please input valid number!")

while True:
    show_menu()
    options = input("Choose menu (1/2/3/4): ")

    if options == "1":
        show_task()
    elif options == "2":
        add_task()
    elif options == "3":
        delete_task()
    elif options == "4":
        print("Thank You! Program finished.")
        break
    else:
        print("Invalid number. Try again.")