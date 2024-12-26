from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from .token_manager import save_token, is_token_expired

@app.route('/create_access_token', methods=['GET', 'POST'])
@login_required
def create_access_token():
    auth_code = request.args.get('auth_code')  # Get auth_code from URL
    if auth_code:
        # Exchange auth code for access token (simulated in this case)
        access_token = save_token(current_user.id, auth_code)
        return redirect(url_for('dashboard'))

    return "Error: Auth code not provided", 400
