import streamlit as st
from utils.database import get_api_keys, save_api_key

def render_login_page():
    """Render the login page for API key input."""
    # Get existing API keys
    api_keys = get_api_keys()
    
    # Display the selectbox from existing API keys
    selected_key = st.selectbox(
        label="Existing OpenAI API Keys", options=api_keys
    )
    
    # A text input box for entering a new key
    new_key = st.text_input(label="New OpenAI API Key", type="password")
    
    login = st.button("Login")
    
    # If new_key is given, add it to database
    # If new_key is not given, use the selected_key
    if login:
        if new_key:
            save_api_key(new_key)
            st.success("Key saved successfully.")
            st.session_state["api_key"] = new_key
            st.rerun()
        else:
            if selected_key:
                st.success(f"Logged in with key '{selected_key}'")
                st.session_state["api_key"] = selected_key
                st.rerun()
            else:
                st.error("API Key is required to login") 