import streamlit as st
from chatbot import get_response

st.title("AI Chatbot using NLP")

user = st.text_input("Ask anything")

if st.button("Send"):

    if user:

        response = get_response(user)

        st.write("Bot:", response)
