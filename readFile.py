import os


def read_last_python_path(entry):
    path = "last_python_path"

    if os.path.isfile(path):
        with open(path, "r") as file:
            # Read the contents of the file
            file_contents = file.read()
            entry.insert(0, file_contents.lstrip())
