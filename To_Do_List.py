import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import os

# File to store tasks
TASKS_FILE = 'tasks.csv'

# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r', newline='') as file:
            reader = csv.reader(file)
            tasks = list(reader)
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(tasks)

# Add task function
def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        tasks.append([task])
        save_tasks(tasks)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Delete task function
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
        del tasks[selected_task_index]
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Edit task function
def edit_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        new_task = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=tasks[selected_task_index][0])
        if new_task:
            tasks[selected_task_index] = [new_task]
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, new_task)
            save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to edit.")

# Load tasks into the listbox
def load_tasks_into_listbox():
    for task in tasks:
        tasks_listbox.insert(tk.END, task[0])
def GUI_TDL():
    # GUI setup
    root = tk.Tk()
    root.title("To-Do List Application")

    tasks = load_tasks()

    tk.Label(root, text="Task:").pack(pady=5)
    task_entry = tk.Entry(root, width=50)
    task_entry.pack(pady=5)

    add_task_button = tk.Button(root, text="Add Task", command=add_task)
    add_task_button.pack(pady=5)

    edit_task_button = tk.Button(root, text="Edit Task", command=edit_task)
    edit_task_button.pack(pady=5)

    delete_task_button = tk.Button(root, text="Delete Task", command=delete_task)
    delete_task_button.pack(pady=5)

    tasks_listbox = tk.Listbox(root, width=50, height=15)
    tasks_listbox.pack(pady=10)

    load_tasks_into_listbox()

    root.mainloop()
