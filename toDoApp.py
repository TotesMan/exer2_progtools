# toDoApp.py
import json
import os

tasks = []
TASKS_FILE = "tasks.json"

class Task:
    def __init__(self, description: str):
        self.description = description

    def to_dict(self):
        return {"Task": self.description}

    @staticmethod
    def from_dict(data):
        return Task(data["Task"])

def loadtasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]
    return []

def savetasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)

def addtask(tasks, description):
    task = Task(description)
    tasks.append(task)
    savetasks(tasks)
    print(f"Task '{description}' added!")

def showTasks():
    if len(tasks) == 0:
        print("\nNo tasks available. Please add one first.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.description}")

def removetask(tasknumber):
    index = tasknumber - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        savetasks(tasks)
        print(f"Task '{removed.description}' has been removed!")
    else:
        print("Invalid task number. Please try again.")

# Main loop
def main():
    global tasks
    tasks = loadtasks()

    while True:
        print("\n=== TO-DO LIST MENU ===")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        print("=======================")

        ch = input("Enter your choice: ")
        if ch == "1":
            t = input("Enter task: ").strip()
            if t:
                addtask(tasks, t)
            else:
                print("Task cannot be empty.")
        elif ch == "2":
            showTasks()
        elif ch == "3":
            if len(tasks) == 0:
                print("No tasks to remove.")
            else:
                try:
                    n = int(input("Enter task number to remove: "))
                    removetask(n)
                except ValueError:
                    print("Please enter a valid number.")
        elif ch == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()
