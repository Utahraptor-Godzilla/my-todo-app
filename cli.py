from functions import *
from time import *
print(f"It is {strftime("%b %d, %Y %H:%M:%S")}.")
while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()
    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos = get_todos()
        todos.append(todo)
        write_todos('todos.txt', todos)
    elif user_action.startswith('show'):
        todos = get_todos('todos.txt')
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}-{item}")
    elif user_action.startswith('edit'):
        try:
            todos = get_todos()
            number = int(user_action[5:])-1
            new_todo = input(f'What would you like to replace "{todos[number].strip('\n')}" with? ')
            todos[number] = new_todo + '\n'
            write_todos('todos.txt', todos)
        except ValueError:
            print("Invalid command.")
            continue
    elif user_action.startswith('complete'):
        try:
            todos = get_todos()
            number = int(user_action[9:])-1
            todos.pop(number)
            write_todos('todos.txt', todos)
        except ValueError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("You have entered an unknown command.")
print("BYE BYE!!!!!!!!!!!!!!!!!!!!!")