import streamlit as st
from chatbot import CollegeChatBot

# Initialize chatbot
bot = CollegeChatBot('intents.json')

# Set up session state to hold chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# App title and input box
st.set_page_config(page_title="College Chatbot", layout="centered")
st.title("📚 AI College Chatbot")
st.write("Ask anything about your college!")

# User input
user_input = st.text_input("You:", "", key="input")

# On input, get response and update chat history
if user_input:
    response = bot.get_response(user_input)
    
    # Append to chat history
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("Bot", response))

# Display chat history
for sender, message in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**🧑‍💻 {sender}:** {message}")
    else:
        st.markdown(f"**🤖 {sender}:** {message}")
