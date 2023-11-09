import tkinter as tk
import subprocess
from threading import Thread
from tkinter import filedialog


def open_folder_dialog(event):
    folder_path = filedialog.askdirectory()
    if folder_path:
        python_path_entry.delete(0, tk.END)
        python_path_entry.insert(0, folder_path)


def execute_command():
    text_widget.delete("1.0", "end")
    path = python_path_entry.get()
    action = python_command_entry.get()
    python = f"{path}\\python.exe"
    pip = f"{path}\\Scripts\\pip.exe"
    command = f"{python} {pip} {action}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               universal_newlines=True)

    def update_text_widget():
        for line in process.stdout:
            text_widget["state"] = "normal"
            text_widget.insert(tk.END, line)
            text_widget.insert(tk.END, "\n")
            text_widget["state"] = "disabled"

        for line in process.stderr:
            text_widget["state"] = "normal"
            text_widget.insert(tk.END, line)
            text_widget.insert(tk.END, "\n")
            text_widget["state"] = "disabled"

        text_widget.see(tk.END)  # Scroll to the end of the text

    # Start a separate thread to update the text widget with command output
    update_thread = Thread(target=update_text_widget)
    update_thread.start()


root = tk.Tk()
root.title("Python Command Line")
root.geometry("500x500")
root.resizable(False, False)

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

execute_button = tk.Button(frame_2, text="Execute Command", command=execute_command)
execute_button.pack(side="left")

text_widget = tk.Text(root, wrap=tk.WORD, height=100)  # Adjust the height here
text_widget.pack(fill="both", expand=True, padx=10, pady=5)
text_widget["state"] = "disabled"

# Create a vertical scrollbar and attach it to the text_widget
scrollbar = tk.Scrollbar(text_widget)
scrollbar.pack(side="right", fill="y")
text_widget.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_widget.yview)

root.mainloop()
