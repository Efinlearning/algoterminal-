from flask import render_template, request, redirect, url_for
from flask_login import login_required
from .fyers_api import generate_auth_code

@app.route('/generate_auth_code', methods=['GET', 'POST'])
@login_required
def generate_auth_code():
    if request.method == 'POST':
        # Assuming client_id and secret_key were saved from the previous form
        client_id = "your_client_id"
        secret_key = "your_secret_key"
        
        auth_code = generate_auth_code(client_id, secret_key)
        
        if auth_code:
            return redirect(url_for('create_access_token', auth_code=auth_code))
        else:
            return "Failed to generate auth code", 400

    return render_template('generate_auth_code.html')
