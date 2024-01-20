def get_todos(filepath='todos.txt'):
    """Reads a text file and returns a list of all the to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(file_path, todos_arg):
    """Writes a list of to-do items in the text file."""
    with open(file_path, 'w') as file_local:
        file_local.writelines(todos_arg)
