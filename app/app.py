from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

# Initialize the Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize the login manager
login_manager = LoginManager()
login_manager.init_app(app)

# Mock database for users (in a real app, this would be a database)
users = {
    "user@example.com": {"password": "password123"},
    "1234567890": {"password": "password123"},
}

class User(UserMixin):
    def __init__(self, id):
        self.id = id

# User loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Login form
class LoginForm(FlaskForm):
    username = StringField('Username (Email/Phone)', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        if username in users and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials"

    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
