import json
import os

DB_FILE = "db.json"

def init_database():
    """Initialize the database file if it doesn't exist."""
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as file:
            db = {"openai_api_keys": [], "chat_history": []}
            json.dump(db, file)

def load_database():
    """Load the database from the file."""
    with open(DB_FILE, "r") as file:
        return json.load(file)

def save_database(db):
    """Save the database to the file."""
    with open(DB_FILE, "w") as file:
        json.dump(db, file)

def get_chat_history():
    """Get the chat history from the database."""
    db = load_database()
    return db.get("chat_history", [])

def save_chat_history(messages):
    """Save the chat history to the database."""
    db = load_database()
    db["chat_history"] = messages
    save_database(db)

def clear_chat_history():
    """Clear the chat history in the database."""
    db = load_database()
    db["chat_history"] = []
    save_database(db)

def get_api_keys():
    """Get the list of API keys from the database."""
    db = load_database()
    return db.get("openai_api_keys", [])

def save_api_key(key):
    """Save a new API key to the database."""
    db = load_database()
    if key not in db["openai_api_keys"]:
        db["openai_api_keys"].append(key)
        save_database(db) 