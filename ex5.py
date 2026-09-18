import streamlit as st

st.title("Average Score")

total_score = st.text_input("Enter total score:")
subjects = st.text_input("Enter number of subjects:")

if st.button("Calculate"):
    try:
        total_score = float(total_score)
        subjects = int(subjects)

        average = total_score / subjects

        st.write("Average Score:", average)

    except ZeroDivisionError:
        st.write("Number of Subjects Cannot Be Zero")