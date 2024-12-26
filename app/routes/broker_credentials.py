from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from flask import Flask

app = Flask(__name__)

# Broker credentials form
class BrokerCredentialsForm(FlaskForm):
    client_id = StringField('Client ID', validators=[DataRequired()])
    secret_key = PasswordField('Secret Key', validators=[DataRequired()])

@app.route('/broker_credentials', methods=['GET', 'POST'])
@login_required
def broker_credentials():
    form = BrokerCredentialsForm()
    if form.validate_on_submit():
        # Save broker credentials in session or database
        client_id = form.client_id.data
        secret_key = form.secret_key.data
        # Normally, store these in the database, but for now, just print them
        print(f"Client ID: {client_id}, Secret Key: {secret_key}")
        return redirect(url_for('generate_auth_code'))

    return render_template('broker_credentials.html', form=form)
