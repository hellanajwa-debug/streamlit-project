import streamlit as st

st.title("Student ID")

student_id = st.text_input("Enter Student ID:")

if st.button("Submit"):
    try:
        student_id = int(student_id)
    except:
        st.write("Invalid Student ID")
    else:
        st.write("Student ID:", student_id)