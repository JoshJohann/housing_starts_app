import streamlit as st

# Streamlit app
st.title('Welcome to the Web App!')

# Input for the first name
first_name = st.text_input("Please enter your first name:")

# Submit button
if st.button('Submit'):
    st.write(f"Happy Birthday, {first_name}!")
