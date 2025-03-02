import streamlit as st
from utils.chat import get_available_models
from utils.database import clear_chat_history

def render_sidebar():
    """Render the sidebar with model selection and clear chat button."""
    # Get available models
    models = get_available_models()
    
    # Create a select box for the models
    st.session_state["openai_model"] = st.sidebar.selectbox(
        "Select OpenAI model", models, index=0
    )
    
    # Add a "Clear Chat" button to the sidebar
    if st.sidebar.button("Clear Chat"):
        clear_chat_history()
        st.session_state.messages = []
        st.rerun() 