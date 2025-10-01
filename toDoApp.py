# toDoApp.py
import json
import os

tasks=[]
TASKS_FILE = "tasks.json"

class Task:
    def __init__(self, description: str):
        self.description = description

    def to_dict(self):
        return {"Task": self.description}

    @staticmethod
    def from_dict(data):
        return Task(data["Task"])
        
def savetasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)
        
def addtask(tasks, description):
    task = Task(description)
    tasks.append(task)
    savetasks(tasks)
    print(f"Task '{description}' added!")
  
def showTasks( ): #CB
    if len(tasks)==0 :
      print("no tasks yet")
    else:
     for i in range (len(tasks)):
      print(i+1,".",tasks[i])

def removetask(tasknumber):
    tasks.pop(tasknumber) 
    print("task removed!!")

def main():
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
            n = int(input("Enter task number to remove: "))
            removetask(n - 1)   
        elif ch == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()





