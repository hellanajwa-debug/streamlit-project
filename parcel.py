import streamlit as st

st.title("Parcel Postage Calculator")

weight = st.text_input("Enter parcel weight (kg):")

if st.button("Calculate"):
    try:
        weight = float(weight)

        if weight <= 2:
            postage = weight * 5
        else:
            postage = weight * 7

        st.write("Parcel Weight:", weight, "kg")
        st.write("Total Postage: RM", postage)

    except:
        st.write("Invalid Weight")