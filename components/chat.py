import streamlit as st
from utils.chat import generate_chat_response, display_chat_history, display_chat_response
from utils.database import save_chat_history

def render_chat_interface(client):
    """Render the chat interface with message history and input."""
    # Display chat messages from history
    display_chat_history(st.session_state.messages)
    
    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            stream = generate_chat_response(
                client, 
                st.session_state.messages, 
                st.session_state["openai_model"]
            )
            response = display_chat_response(stream)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Save chat history to database
        save_chat_history(st.session_state.messages) 