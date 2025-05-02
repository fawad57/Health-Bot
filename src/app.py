from config import decode_api_key, encoded_api_key
from chat import initialize_chat
from streamlit_app import main

if __name__ == "__main__":
    # Initialize chat with API configuration
    initialize_chat({"decode_api_key": decode_api_key, "encoded_api_key": encoded_api_key})
    # Run the Streamlit app
    main()