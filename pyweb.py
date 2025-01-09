import streamlit as st
import testli as tt

todos=tt.Realtd()
st.title("My TODO app")
st.subheader("Lists of Tasks Todo")
cnt=0
for i in todos:
    st.checkbox(i,key=cnt)
    cnt+=1
st.text_input(label="",placeholder="Enter a New Task To Add")