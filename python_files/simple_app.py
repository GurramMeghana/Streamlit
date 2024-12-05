import streamlit as st

# App Title
st.title("Echo Your Input")

# User Input
user_input = st.text_input("Enter something:")

# Display Output
if user_input:
    st.write(f"You entered: {user_input}")
