import streamlit as st

st.title("Ticket Price")

price = st.text_input("Enter ticket price:")

if st.button("Submit"):
    try:
        price = float(price)
    except:
        st.write("Invalid Price")
    else:
        st.write("Ticket Price:", price)