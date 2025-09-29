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
        # Added header before listing tasks
        print("Your Tasks:")
        # Using enumerate for cleaner iteration
        for i, task in enumerate(tasks, start=1):
            print(i, ".", task)

# Remove a Task
def remove_Task(tasknum):
    # remove_Task expects a 1-based number; convert to 0-based index
    index = tasknum - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Task '{removed}' has been removed!")
    else:
        print("Invalid task number. Please try again.")

# Centralized helper for integer input
def parse_int(prompt):
    """Prompt the user and return an int, or None if invalid."""
    try:
        return int(input(prompt))
    except ValueError:
        return None

# Main loop
def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add a Task")
        print("2. Show Tasks")
        print("3. Remove a Task")
        print("4. Exit")
        chc = input("Enter choice: ").strip()

        if chc == "1":
            task = input("Enter task: ").strip()
            if task:
                add_Task(task)
            else:
                print("Task cannot be empty.")

        elif chc == "2":
            show_Tasks()

        elif chc == "3":
            if len(tasks) == 0:
                print("No tasks to remove.")
            else:
                num = parse_int("Enter task no. to remove: ")
                if num is None:
                    print("Please enter a valid number.")
                else:
                    remove_Task(num)

        elif chc == "4":
            print("Exiting To-Do App. Goodbye!")
            break

        else:
            print("Please input a valid choice (1–4).")

# Run program
main()
