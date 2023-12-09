def remember_last_python(entry):
    # Open the file in write mode (creates a new file if it doesn't exist)
    with open("last_python_path", "w") as file:
        # Write the text to the file
        file.write(entry.get().lstrip())
