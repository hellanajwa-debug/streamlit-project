import streamlit as st

st.title("Temperature Input")

temperature = st.text_input("Enter temperature:")

if st.button("Display"):
    try:
        temperature = float(temperature)
        st.write("Temperature:", temperature)

    except:
        st.write("Invalid Temperature")