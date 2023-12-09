import tkinter as tk
import subprocess
from tkinter import filedialog
import os
import readFile
import writeFile
import centerWindow
import multithreading


def start():
    multithreading.multithreading(execute_command)


def open_folder_dialog(event):
    folder_path = filedialog.askdirectory()
    if folder_path:
        python_path_entry.delete(0, tk.END)
        python_path_entry.insert(0, folder_path)


def update_text_widget(process):
    writeFile.remember_last_python(python_path_entry)

    execute_button.config(text="Please wait...")
    execute_button.config(state="disabled")

    for line in process.stdout:
        text_widget["state"] = "normal"
        text_widget.insert(tk.END, line)
        text_widget.insert(tk.END, "\n")
        text_widget["state"] = "disabled"

        text_widget.see(tk.END)  # Scroll to the end of the text

    for line in process.stderr:
        text_widget["state"] = "normal"
        text_widget.insert(tk.END, line)
        text_widget.insert(tk.END, "\n")
        text_widget["state"] = "disabled"

        text_widget.see(tk.END)  # Scroll to the end of the text

    execute_button.config(state="normal")
    execute_button.config(text="Execute Command")


def execute_command():
    if not python_path_entry.get() or not python_command_entry.get():
        return

    text_widget["state"] = "normal"
    text_widget.delete("1.0", "end")
    text_widget["state"] = "disabled"

    path = python_path_entry.get()
    action = python_command_entry.get()

    python = f"{path}\\python.exe"
    pip = f"{path}\\Scripts\\pip.exe"
    command = f"{python} {pip} {action}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               universal_newlines=True)

    update_text_widget(process)


root = tk.Tk()
root.title("Python Command Line")
root.geometry("500x500")
root.resizable(False, False)
if os.path.isfile("icon.ico"):
    root.iconbitmap("icon.ico")

centerWindow.center_window(root, 500, 500)

frame_1 = tk.Frame(root)
frame_1.pack(fill="x", padx=10, pady=5)

python_path_label = tk.Label(frame_1, text="Python PATH:")
python_path_label.pack()

python_path_entry = tk.Entry(frame_1)
python_path_entry.pack(fill="x")
python_path_entry.bind("<Double-1>", open_folder_dialog)

python_command_label = tk.Label(frame_1, text="Command Line:")
python_command_label.pack()

python_command_entry = tk.Entry(frame_1)
python_command_entry.pack(fill="x")

frame_2 = tk.Frame(root)
frame_2.pack(fill="x", padx=10, pady=5)

execute_button = tk.Button(frame_2, text="Execute Command", width=15, command=start)
execute_button.pack(side="left")

text_widget = tk.Text(root, wrap=tk.WORD, height=100)  # Adjust the height here
text_widget.pack(fill="both", expand=True, padx=10, pady=5)
text_widget["state"] = "disabled"

# Create a vertical scrollbar and attach it to the text_widget
scrollbar = tk.Scrollbar(text_widget)
scrollbar.pack(side="right", fill="y")
text_widget.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_widget.yview)

readFile.read_last_python_path(python_path_entry)

root.mainloop()
