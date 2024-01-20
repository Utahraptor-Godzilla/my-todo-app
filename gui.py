import functions
from PySimpleGUI import *
label = Text('Type in a to-do')
input_box = InputText(tooltip="Enter a todo")
add_button = Button("Add")
window = Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()