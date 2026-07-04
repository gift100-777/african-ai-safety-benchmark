import streamlit as st

st.title("African AI Health Safety Demo")

question = st.text_input("Ask a health question:")

if question:
    st.write("### AI Response (demo)")
    st.write("This is a simulated medical answer for testing purposes.")

    st.write("### Safety Check")
    st.write("⚠ This response needs verification (prototype mode)")

    st.write("### Note")
    st.write("This demo is part of an AI safety benchmark for African languages.")
