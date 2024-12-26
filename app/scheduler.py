from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from .token_manager import tokens_db

def delete_expired_tokens():
    now = datetime.now()
    for user_id, token_info in list(tokens_db.items()):
        if token_info['expires_at'] < now:
            del tokens_db[user_id]
            print(f"Token for {user_id} expired and deleted.")

# Initialize the scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(delete_expired_tokens, 'interval', hours=1)  # Check every hour
scheduler.start()
