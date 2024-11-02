import streamlit as st
import requests
import ollama
from typing import Dict, Generator

# Set up the page title and layout
st.set_page_config(page_title="Know Your Health", layout="centered")

# Title of the app
st.title("Know Your Health")

# Function to generate response using Ollama
def generate_ollama_response(model_name: str, messages: Dict) -> Generator:
    stream = ollama.chat(model=model_name, messages=messages, stream=True)
    for chunk in stream:
        yield chunk['message']['content']

# Create two tabs
tab1, tab2 = st.tabs(["Input Your Health", "Talk with me"])

# Tab 1: Input Your Health
with tab1:
    st.header("Input Your Health")

    # Individu Section
    st.subheader("Individu")
    age = st.text_input("Enter your age:", placeholder="e.g., 30")
    gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])

    # Activity Section
    st.subheader("Activity")
    daily_activity = st.text_input("Describe your daily activity level:", placeholder="e.g., moderate")

    # Goals Section
    st.subheader("Goals")
    health_concern = st.text_input("Enter your primary health concern:", placeholder="e.g., hypertension")

    # Generate text based on input using Ollama with "llama3.2:latest"
    if st.button("Generate Health Insights"):
        if age and gender and daily_activity and health_concern:
            # Define a custom prompt based on inputs
            health_prompt = (
                f"You are a health advisor. Based on the user's age ({age}), gender ({gender}), "
                f"health concern ({health_concern}), and activity level ({daily_activity}), "
                f"provide tailored health advice in Bahasa Indonesia."
            )
            
            # Call Ollama API with the generated prompt
            messages = [{"role": "user", "content": health_prompt}]
            response = ''.join(generate_ollama_response("llama3.2:latest", messages))
            
            st.write("Health Insights:")
            st.write(response)
        else:
            st.warning("Please fill in all fields to generate insights.")
# Tab 2: Talk with me
with tab2:
    st.header("Chat with Me")

    # Setting up chat history
    if "selected_model" not in st.session_state:
        st.session_state.selected_model = ""
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Model selection and chat display
    st.session_state.selected_model = st.selectbox(
        "Please select the model:", [model["name"] for model in ollama.list()["models"]]
    )
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # User input and response in chat
    if prompt := st.chat_input("How could I help you?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = st.write_stream(generate_ollama_response(
                st.session_state.selected_model, st.session_state.messages
            ))
            st.session_state.messages.append({"role": "assistant", "content": response})
