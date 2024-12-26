from flask import render_template
from flask_login import login_required, current_user
from .fyers_api import get_option_chain
from .token_manager import is_token_expired

@app.route('/option_chain')
@login_required
def option_chain():
    if is_token_expired(current_user.id):
        return redirect(url_for('login'))  # Redirect to login if token expired

    access_token = "your_access_token_here"  # Replace with the actual access token
    option_data = get_option_chain(access_token)

    if option_data:
        return render_template('option_chain.html', option_data=option_data)
    else:
        return "Failed to fetch option chain data", 500
