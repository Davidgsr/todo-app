def get_todos(filepath='todos.txt') -> list:
    """ Read a text file and return the list of to-do items. """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath='todos.txt'):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        new_todos = [item.strip("\n") for item in todos] # Remover as quebras de linha extras

        for index, item in enumerate(new_todos):
            row = f"{index + 1}. {item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print('Your command is not valid.')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            todo_to_remove = todos[number - 1].title()
            todos.pop(number - 1)

            write_todos(todos)

            print(f"Todo {todo_to_remove.strip("\n")} was removed from the list")
        except IndexError:
            print('There is no item with that number.')
            continue
        except ValueError:
            print('Type the number of todo to complete with the command "Complete..."')

    elif user_action.startswith('exit'):
        break
    else:
        print('Choose a Valid Option')