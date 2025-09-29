# toDoApp.py

tasks=[]
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

def removetask(tasknumber): #Jaspur
    tasks.pop(tasknumber) 
    print("task removed!!")

def main():
  # Totes
    while True:
        print("1 Add Task")
        print("2.Show Tasks")
        print("3.Remove Task")
        print("4- Exit")
        ch = input("enter choice : ")
        if ch=="1":
            t = input("enter task : ")
            addtask(t)
        elif ch=="2":
            showTasks()
        elif ch=="3":
            n=int(input("enter task no to remove: "))
            removetask(n)   
        elif ch=="4":
            break;
        else:
            print("wrong choice!!")
main()



