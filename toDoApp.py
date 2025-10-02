import json
import os
import tkinter as tk
from tkinter import messagebox, font as tkfont

# File where tasks are stored
TASKS_FILE = "tasks.json"

# ---------------- Task Class ----------------
class Task:
    def __init__(self, description: str):
        # Each task has a description
        self.description = description

    def to_dict(self):
        # Convert task to dictionary for saving in JSON
        return {"Task": self.description}

    @staticmethod
    def from_dict(data):
        # Create a Task object from dictionary
        return Task(data["Task"])

# ---------------- Task Management ----------------
def load_tasks():
    # Load tasks from JSON file if it exists
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            data = json.load(f)
            return [Task.from_dict(item) for item in data]
    return []  # Return empty list if file doesn't exist

def save_tasks(tasks):
    # Save tasks to JSON file
    with open(TASKS_FILE, "w") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)

def add_task(tasks, description, listbox, task_entry):
    # Add a new task
    if description.strip() == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return
    task = Task(description)
    tasks.append(task)  # Add task to list
    insert_task_to_listbox(listbox, task.description)  # Show task in listbox
    save_tasks(tasks)  # Save tasks to file
    task_entry.delete(0, tk.END)  # Clear input
    messagebox.showinfo("Success", f"Task '{description}' added!")

def remove_task(tasks, listbox):
    # Remove selected task
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a task to remove.")
        return
    index = selected[0]
    removed_task = tasks.pop(index)  # Remove from list
    listbox.delete(index)  # Remove from GUI
    save_tasks(tasks)  # Save updated tasks
    messagebox.showinfo("Removed", f"Task '{removed_task.description}' removed!")

# Insert task into Listbox with alternating colors
def insert_task_to_listbox(listbox, task_desc):
    index = listbox.size()
    listbox.insert(tk.END, task_desc)
    # Alternate colors for readability
    if index % 2 == 0:
        listbox.itemconfig(index, bg="#e0f7fa", fg="#006064")
    else:
        listbox.itemconfig(index, bg="#b2ebf2", fg="#004d40")

# ---------------- GUI Setup ----------------
def main():
    tasks = load_tasks()  # Load tasks when app starts

    root = tk.Tk()
    root.title("To-Do List System")
    root.geometry("500x600")
    root.minsize(400, 400)  # Minimum window size
    root.configure(bg="#00796b")  # Background color

    # Fonts
    title_font = tkfont.Font(family="TkDefaultFont", size=20, weight="bold")
    list_font = tkfont.Font(family="TkDefaultFont", size=14)
    entry_font = tkfont.Font(family="TkDefaultFont", size=14)
    button_font = tkfont.Font(family="TkDefaultFont", size=12, weight="bold")
    remove_button_font = tkfont.Font(family="TkDefaultFont", size=14, weight="bold")

    # Title label
    tk.Label(root, text="Your To-Do List", font=title_font,
             fg="white", bg="#00796b").pack(pady=15)

    # Frame for listbox (tasks)
    list_frame = tk.Frame(root, bg="#00796b")
    list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

    listbox = tk.Listbox(list_frame, bd=0, highlightthickness=0, font=list_font)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Scrollbar for listbox
    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    # Load tasks into the listbox
    for task in tasks:
        insert_task_to_listbox(listbox, task.description)

    # Frame for entry and add button
    entry_frame = tk.Frame(root, bg="#00796b")
    entry_frame.pack(fill=tk.X, padx=20, pady=10)

    task_entry = tk.Entry(entry_frame, font=entry_font)
    task_entry.grid(row=0, column=0, sticky="we", padx=(0, 5))
    entry_frame.columnconfigure(0, weight=1)  # Make entry expand with window

    add_btn = tk.Button(entry_frame, text="Add Task", bg="#004d40", fg="white",
                        font=button_font, activebackground="#00695c", activeforeground="white",
                        command=lambda: add_task(tasks, task_entry.get(), listbox, task_entry))
    add_btn.grid(row=0, column=1)

    # Remove button
    remove_btn = tk.Button(root, text="REMOVE SELECTED TASK", bg="#e53935", fg="white",
                           font=remove_button_font, activebackground="#ef5350",
                           activeforeground="white", command=lambda: remove_task(tasks, listbox))
    remove_btn.pack(fill=tk.X, padx=20, pady=10)

    # Exit button
    exit_btn = tk.Button(root, text="Exit", bg="#616161", fg="white", font=button_font,
                         activebackground="#9e9e9e", activeforeground="white",
                         command=root.destroy)
    exit_btn.pack(fill=tk.X, padx=20, pady=5)

    root.mainloop()  # Start the GUI loop


if __name__ == "__main__":
    main()

