import streamlit as st

st.title("🔥 Test App")
st.write("Hello World!")
st.write("If you can see this, Streamlit is working!")

# Test basic functionality
if st.button("Click me"):
    st.write("Button clicked!")

# Test input
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")