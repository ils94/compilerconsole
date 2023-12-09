def read_last_python_path(entry):
    # Open the file in read mode
    with open("last_python_path", "r") as file:
        # Read the contents of the file
        file_contents = file.read()
        entry.insert(0, file_contents.lstrip())
