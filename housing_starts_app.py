import streamlit as st

# Streamlit app
st.title('an important message awaits')

# Input for the first name
first_name = st.text_input("Enter your first name:")

# Submit button
if st.button('Submit'):
    st.write(f"You're so gay, {first_name}!")
