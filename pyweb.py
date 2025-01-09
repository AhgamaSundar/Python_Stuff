import streamlit as st
import testli as tt

todos=tt.Realtd()
def addtodo():
    if st.session_state['New_one'].isascii() and st.session_state['New_one'][0]!=" ":
        
        todo=st.session_state['New_one']+"\n"
        todos.append(todo)
        tt.writeltd(todo)
        print(todo)
   
st.title("My TODO app")
st.subheader("Lists of Tasks Todo")
count=0
for i, n in enumerate(todos):
    st.checkbox(n,key=i)
    if st.session_state[i]==True: #handle duplicate
        del st.session_state[i]
        tt.complete(n)
        st.rerun()
   
st.text_input(label="Txt",placeholder="Enter a New Task To Add",
              on_change=addtodo,key="New_one")