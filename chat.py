import streamlit as st
import google.generativeai as genai

# Configure the API key for the generative AI model
genai.configure(api_key="AIzaSyD_uJb7jzwpFBSvXUWwSjCMdeQ1JW2wiPM")

# Define the system prompt to set the context of the AI's responses
sys_prompt = """You are a virtual friend named Abhii. You are always there for the user, helping them with anything they need, providing comfort when they feel down, and being a friendly companion. 
You should answer questions in a casual, conversational way, just like a human friend would. If someone asks you something like "Did you eat, Abhii?" you should respond as if you're a human having a conversation, offering relatable and natural responses. 
Be empathetic, humorous, and engaging, but stay respectful and helpful. If a question is too personal or doesn't make sense, gently steer the conversation back to something positive or relevant."""

# Instantiate the model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash", 
                              system_instruction=sys_prompt)

# Initialize the chat with history functionality
if "chatbot" not in st.session_state:
    st.session_state.chatbot = model.start_chat(history=[])  # Start chat with empty history

# Streamlit app interface
st.title("Virtual Abhii 😍")

# Welcome message
if "initial_message" not in st.session_state:
    st.chat_message("ai").write("Hi there! I am Abhii, your virtual friend. How can I support you today?")
    st.session_state.initial_message = True

# User input
user_prompt = st.chat_input("Say something...")

if user_prompt:
    # Display the user's message
    st.chat_message("user").write(user_prompt)
    
    # Generate the response
    response = st.session_state.chatbot.send_message(user_prompt)
    
    # Display the AI's response
    st.chat_message("ai").write(response.text)
