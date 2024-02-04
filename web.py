from functions import *
from streamlit import *
todos = get_todos()
def add_todo():
    todo = session_state["new_todo"]+'\n'
    todos.append(todo)
    write_todos(todos)

title("My Todo App")
subheader("This is my todo app.")
write("This app is to increase your productivity.")
for todo in todos:
    checkbox(todo)
text_input(label="Enter a todo:", placeholder="Add a new todo", on_change=add_todo, key="new_todo")
print("Hello")
session_state