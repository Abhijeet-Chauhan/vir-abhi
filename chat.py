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

# Set up the Streamlit application interface
st.title("Virtual Abhii 😘")

# Input field for user prompt
user_prompt = st.text_input("Enter your query:", placeholder="Type your query here...")

# Button to generate an answer
btn_click = st.button("Generate Answer")

# If the button is clicked and the user has entered a query
if btn_click and user_prompt:
    # Generate the response
    response = model.generate_content(user_prompt)
    
    # Check if the response contains candidates and handle accordingly
    if response and hasattr(response, 'candidates') and response.candidates:
        # Get the text content from the first candidate
        answer = response.candidates[0].content.parts[0].text
        st.write(answer)
    else:
        # Handle case when no response is generated
        st.write("Sorry, I couldn't generate an answer. Please try again.")
