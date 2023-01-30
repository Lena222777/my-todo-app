import streamlit as st
import functions
#streamlit run web_todo.py

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_in_file(todos)



st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_in_file(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter a todo", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

