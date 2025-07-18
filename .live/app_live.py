#app.py
# streamlit run app.py

import streamlit as st

st.set_page_config(
    page_title="Survey: Your Experience with Python and SQL",
    page_icon="🎓",
    layout="wide"   
)

st. title("Streamlit Workshop Intro")

st.write("This is a simple Streamlit app to demonstrate the basics of Streamlit.")
st.header("Welcome to the Streamlit Workshop!")
st.subheader("What is Streamlit?")
st.caption("Streamlit is an open-source app framework for Machine Learning and Data Science projects. It allows you to create beautiful web apps with minimal effort.")

st.markdown("""
## Key Features of Streamlit:
- **Easy to Use**: Write Python scripts and turn them into interactive web apps.
""")

st.divider()

st.html("<p>This is a custom HTML component!</p>")


st.button("Read more")

if st.button("Click me!"):
    st.write("You clicked the button!")
else:
    st.write("Good bye!")
