import tkinter as tk
from tkinter import Menu

def delete_task(event):
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)

def exit_program():
    root.quit()

root = tk.Tk()
root.title("Akimov-ToDo")
root.config(bg="blue")

menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu, tearoff=0, bg="orange", fg="white")
menu.add_cascade(label="Akimov-ToDo", menu=file_menu)
file_menu.add_command(label="Exit", command=exit_program)

instructions_label = tk.Label(root, text="Right-click to delete a task", bg="blue", fg="white")
instructions_label.pack()

tasks_listbox = tk.Listbox(root)
tasks_listbox.pack()
tasks_listbox.bind('<Button-3>', delete_task)

task_entry = tk.Entry(root)
task_entry.pack()

task_counter = 0

def add_task():
    global task_counter
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        color = 'light pink' if task_counter % 2 == 0 else 'lightblue'
        tasks_listbox.itemconfig(tk.END, {'bg': color})
        task_counter += 1
        task_entry.delete(0, tk.END)

add_task_button = tk.Button(root, text="Add Task", command=add_task)
add_task_button.pack()

root.mainloop()