from flask import Flask, render_template, request, redirect, url_for, session
import os
import logging
from logging.handlers import RotatingFileHandler
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

#Admin credentials
USERS = {
    'dp': 'Welcome987*',
    'prem': 'prem',
    # Add more users as needed
}

#logs

log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = RotatingFileHandler('app.log', maxBytes=1024 * 1024, backupCount=10)
file_handler.setFormatter(log_formatter)
file_handler.setLevel(logging.INFO)

logging.getLogger().addHandler(file_handler)
logging.getLogger().setLevel(logging.INFO)


#Login Required
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function


# Directory to store certificates
CERTS_DIR = 'certs'

@app.route('/admin')
def index():
    return render_template('admin_login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in USERS and USERS[username] == password:
        session['logged_in'] = True
        session['username'] = username  # Store username in session
        print("Logged in as: "+ username)
        return redirect(url_for('admin_dashboard'))
    else:
        return render_template('admin_login.html', error='Invalid credentials')


@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if session.get('logged_in'):
        return render_template('admin.html')
    else:
        return redirect(url_for('admin'))

@app.route('/logout' , methods=['POST'])
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('admin'))

@app.route('/create_folder_and_upload', methods=['POST'])
def create_folder_and_upload():
    if request.method == 'POST':
        co = request.form['co']
        folder_name = request.form['folderName']
        certificates = request.files.getlist('certificates[]')

        # Create directory for the CO if it doesn't exist
        co_dir = os.path.join(CERTS_DIR, co)
        os.makedirs(co_dir, exist_ok=True)

        # Create directory for the event under CO directory
        event_dir = os.path.join(co_dir, folder_name)
        os.makedirs(event_dir, exist_ok=True)

        # Save uploaded certificates to the event directory
        for certificate in certificates:
            certificate.save(os.path.join(event_dir, certificate.filename))

        # Render the HTML template with the success message
        return render_template('upload_success.html')


if __name__ == '__main__':
    app.run(debug=True)