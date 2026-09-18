import streamlit as st

st.title("Student Mark")

mark = st.text_input("Enter student mark:")

if st.button("Submit"):
    try:
        mark = int(mark)
        st.write("Student Mark:", mark)
    except:
        st.write("Invalid Mark")