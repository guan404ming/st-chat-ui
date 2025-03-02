# Streamlit Chat UI

A chat interface application built with Streamlit and Google Gemini API.

## Project Structure

```
.
├── app.py                  # Main application entry point
├── components/             # UI components
│   ├── __init__.py
│   ├── chat.py             # Chat interface component
│   ├── login.py            # Login interface component
│   └── sidebar.py          # Sidebar component
├── utils/                  # Utility tools
│   ├── __init__.py
│   ├── chat.py             # Chat-related functions
│   └── database.py         # Database operations
├── db.json                 # Data storage file
└── requirements.txt        # Project dependencies
```

## Features

- Chat with Google Gemini API
- Support for multiple Gemini models
- Save and load chat history
- Manage API keys
- Clean user interface

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/st-chat-ui.git
   cd st-chat-ui
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   streamlit run app.py
   ```

## Usage

1. When running for the first time, you need to provide a Google Gemini API key
2. Select the desired Gemini model
3. Start chatting!

## Dependencies

- streamlit
- openai
- python-dotenv
- bs4

## License

MIT 