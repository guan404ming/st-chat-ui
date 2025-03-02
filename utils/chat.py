from openai import OpenAI
import streamlit as st

def get_available_models():
    """Get the list of available models."""
    return [
        "gemini-2.0-flash",
        "gemini-2.0-flash-lite-preview-02-05",
        "gemini-1.5-flash",
        "gemini-1.5-pro",
    ]

def create_openai_client(api_key):
    """Create an OpenAI client with the given API key."""
    return OpenAI(
        api_key=api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/",
    )

def generate_chat_response(client, messages, model):
    """Generate a chat response using the OpenAI API."""
    stream = client.chat.completions.create(
        model=model,
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in messages
        ],
        stream=True,
    )
    return stream

def display_chat_history(messages):
    """Display the chat history in the Streamlit app."""
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def display_chat_response(stream):
    """Display the chat response in the Streamlit app."""
    return st.write_stream(stream) 