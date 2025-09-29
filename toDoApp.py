# toDoApp.py

# Task list
tasks = []

# Add a Task
def add_Task(task):
    tasks.append(task)
    print(f"Task '{task}' has been added!")

# Show Tasks
def show_Tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])

# Remove a Task
def remove_Task(tasknum):
    index = tasknum - 1  # adjust for 1-based input
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Task '{removed}' has been removed!")
    else:
        print("Invalid task number. Please try again.")

# Main loop
def main():
    while True:
        print("\n====== To-Do App ======")
        print("1. Add a Task")
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
                try:
                    num = int(input("Enter task no. to remove: "))
                    remove_Task(num)
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif chc == "4":
            print("Exiting To-Do App. Goodbye!")
            break

        else:
            print("Please input a valid choice (1–4).")

# Run program
main()
