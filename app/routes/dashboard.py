from flask import render_template, redirect, url_for
from flask_login import login_required
from .token_manager import is_token_expired

@app.route('/dashboard')
@login_required
def dashboard():
    if is_token_expired(current_user.id):
        return redirect(url_for('login'))  # Redirect to login if token expired

    return render_template('dashboard.html')
