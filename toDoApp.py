# toDoApp.py

# Initialize Task list
tasks = []

# Adds a Task to the list
def add_Task(task):
    tasks.append(task)
    print("Task added!")

# Shows all Tasks
def show_Tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])

# Deletes a Task
def remove_Task(tasknum):
    # convert 1-based user input to 0-based index
    index = tasknum - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Task '{removed}' has been removed!")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n1. Add a Task")
        print("2. Show Tasks")
        print("3. Remove a Task")
        print("4. Exit")
        chc = input("Enter choice: ")

        if chc == "1":
            task = input("Enter task: ")
            add_Task(task)

        elif chc == "2":
            show_Tasks()

        elif chc == "3":
            if len(tasks) == 0:
                print("No tasks to remove.")
            else:
                num = int(input("Enter task no. to remove: "))
                remove_Task(num)

        elif chc == "4":
            break

        else:
            print("Please input a valid choice!")

main()
