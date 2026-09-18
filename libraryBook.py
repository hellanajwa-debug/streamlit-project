import streamlit as st

st.title("Library Book Type")

number = st.number_input(
    "Enter number of books:",
    min_value=1,
    step=1
)

if st.button("Display"):

    for i in range(number):
        book_type = st.selectbox(
            "Select book type for Book " + str(i + 1),
            ["Fiction", "Non-Fiction", "Reference"]
        )

        if book_type:
            st.write("Selected Book Type:", book_type)