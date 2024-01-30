from functions import *
from PySimpleGUI import *
from time import *
theme("DarkTeal")
clock = Text("", key="clock")
label = Text('Type in a to-do')
input_box = InputText(tooltip="Enter a todo", key="todo")
add_button = Button("Add")
list_box = Listbox(values=get_todos(), key='todos', enable_events=True, size=(45, 10))
edit_button = Button("Edit")
complete_button = Button("Complete")
exit_button = Button("Exit")
window = Window('My To-Do App', layout=[[clock], [label], [input_box, add_button], [list_box, edit_button, complete_button], [exit_button]], font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=strftime("%b %d, %Y %H:%M:%S"))
    closed = False
    print(event)
    print(values)
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values['todo']
            todos.append(new_todo+'\n')
            write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                popup("Please select an item first.", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = get_todos()
                todos.remove(todo_to_complete)
                write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                popup("Please select an item first.", font=("Helvetica", 20))
        case "Exit":
            break
        case "todos":
            if not values['todos']:
                continue
            window['todo'].update(value=values['todos'][0])
        # case WIN_CLOSED:
        #     break
window.close()
# import PySimpleGUI as psg
# names = []
# lst = psg.Listbox(names, size=(20, 4), font=('Arial Bold', 14), expand_y=True, enable_events=True, key='-LIST-')
# layout = [[psg.Input(size=(20, 1), font=('Arial Bold', 14), expand_x=True, key='-INPUT-'),
#    psg.Button('Add'),
#    psg.Button('Remove'),
#    psg.Button('Exit')],
#    [lst],
#    [psg.Text("", key='-MSG-', font=('Arial Bold', 14), justification='center')]
# ]
# window = psg.Window('Listbox Example', layout, size=(600, 200))
# while True:
#    event, values = window.read()
#    print(event, values)
#    if event in (psg.WIN_CLOSED, 'Exit'):
#       break
#    if event == 'Add':
#       names.append(values['-INPUT-'])
#       window['-LIST-'].update(names)
#       msg = "A new item added : {}".format(values['-INPUT-'])
#       window['-MSG-'].update(msg)
#    if event == 'Remove':
#       val = lst.get()[0]
#       names.remove(val)
#       window['-LIST-'].update(names)
#       msg = "A new item removed : {}".format(val)
#       window['-MSG-'].update(msg)
# window.close()
# class Pleasantries:
#     def hi(self, name):
#         return f"Hello {name}!"
#     def salut(self, name="Nom"):
#         return f"Salut {name}!"
#
#
# bye = Pleasantries().salut("la chien")
# print(bye)