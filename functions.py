import os

FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH) -> list:
    """Read a text file and return the list of to-do items."""

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    
    todos_local = [todo.strip() + '\n' for todo in todos_local]

    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list in the text file."""


    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)