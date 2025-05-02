import base64

# API Configuration
encoded_api_key = "QUl6YVN5QWwyclhPcW9pMlpveFE2Q1Z3T1ZqUURHeXBBZTNIVFVn"

def decode_api_key(encoded_api_key):
    """Decode the base64 encoded API key."""
    decoded_bytes = base64.b64decode(encoded_api_key.encode("utf-8"))
    decoded_str = str(decoded_bytes, "utf-8")
    return decoded_str