from datetime import datetime, timedelta

# Simulate a token database with a dictionary
tokens_db = {}

# Function to save the token with expiration time
def save_token(user_id, auth_code):
    access_token = f"access_token_{user_id}"  # Simulate access token
    expiration_time = datetime.now() + timedelta(hours=12)  # Token expires in 12 hours
    tokens_db[user_id] = {'access_token': access_token, 'expires_at': expiration_time}
    return access_token

# Function to check if the token is expired
def is_token_expired(user_id):
    token_info = tokens_db.get(user_id)
    if token_info:
        return datetime.now() > token_info['expires_at']
    return True  # If no token found, consider expired
