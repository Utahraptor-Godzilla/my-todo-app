from functions import *
from streamlit import *
title("My Todo App")
subheader("This is my todo app.")
write("This app is to increase your productivity.")
todos = get_todos()
for todo in todos:
    checkbox(todo)
text_input(label="Enter a todo:", placeholder="Add a new todo")