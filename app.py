import streamlit as st
from utils.database import init_database, get_chat_history
from utils.chat import create_openai_client
from components.sidebar import render_sidebar
from components.login import render_login_page
from components.chat import render_chat_interface

def main():
    """Main application function."""
    # Initialize the database
    init_database()
    
    # Initialize session state for messages if not exists
    if "messages" not in st.session_state:
        st.session_state.messages = get_chat_history()
    
    # Check if user is logged in
    if "api_key" in st.session_state and st.session_state.api_key:
        # Create OpenAI client
        client = create_openai_client(st.session_state.api_key)
        
        # Render sidebar
        render_sidebar()
        
        # Render chat interface
        render_chat_interface(client)
    else:
        # Render login page
        render_login_page()

if __name__ == "__main__":
    main() 