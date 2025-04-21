import tkinter as tk
from tkinter import messagebox
import json
import os


TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []


def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)


def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "done": False})
        save_tasks()
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("error ", "Enter the task!")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        del tasks[selected_index]
        save_tasks()
        update_listbox()
    except IndexError:
        messagebox.showwarning("Error ", "Select the task to delete!")

def complete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index]["done"] = not tasks[selected_index]["done"]
        save_tasks()
        update_listbox()
    except IndexError:
        messagebox.showwarning("Error ", "Select a task to complete!")

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔" if task["done"] else "❌"
        task_listbox.insert(tk.END, f"{status} {task['task']}")

tasks = load_tasks()

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)
add_button = tk.Button(root, text="add", command=add_task)
add_button.pack()

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

complete_button = tk.Button(root, text="Mark as completed", command=complete_task)
complete_button.pack()
delete_button = tk.Button(root, text="delete ", command=delete_task)
delete_button.pack()

update_listbox()

root.mainloop()


