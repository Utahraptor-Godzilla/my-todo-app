from functions import *
from PySimpleGUI import *
label = Text('Type in a to-do')
input_box = InputText(tooltip="Enter a todo", key="todo")
add_button = Button("Add")
window = Window('My To-Do App', layout=[[label], [input_box, add_button]], font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values['todo']
            todos.append(new_todo+'\n')
            write_todos(todos)
        case WIM_CLOSED:
            break
window.close()
