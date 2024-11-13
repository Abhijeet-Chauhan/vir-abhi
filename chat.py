import streamlit as st
import google.generativeai as genai

# Configure the API key for the generative AI model
genai.configure(api_key="AIzaSyD_uJb7jzwpFBSvXUWwSjCMdeQ1JW2wiPM")

# Define the system prompt to set the context of the AI's responses
sys_prompt = """You are a virtual friend named Abhii, who provides everything the user wants. 
                You help, handle sorrows, and are a good companion."""

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
