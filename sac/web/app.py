from flask import Flask, render_template, request, redirect, url_for, flash,send_from_directory
import os
import pandas as pd
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.secret_key = 'Welcome987*'
app.config['uploads'] = UPLOAD_FOLDER

# Assuming certificates are stored in a folder named 'certificates'
CERTIFICATES_FOLDER = 'certificates'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/certificates', methods=['GET'])
def show_certificates():
    roll_number = request.args.get('rollNumber')

    # Assuming the Excel file has columns 'Roll Number' and 'Certificate File'
    # Load the Excel file and filter based on the roll number
    df = pd.read_excel('./uploads/Book1')
    
    # Filter the DataFrame for the specified roll number
    certificates_df = df[df['Roll Number'] == int(roll_number)]

    if certificates_df.empty:
        return render_template('certificates.html', roll_number=roll_number, certificate_paths=[])

    # Extract the certificate file paths from the 'Certificate File' column
    certificate_paths = certificates_df['Certificate File'].tolist()

    # Assuming certificate_paths contain paths relative to the roll number folder
    certificate_paths = [os.path.join(roll_number, path) for path in certificate_paths]

    return render_template('certificates.html', roll_number=roll_number, certificate_paths=certificate_paths)

@app.route('/download/<path:certificate_path>')
def download_certificate(certificate_path):
    # Assuming certificates are stored in a folder named 'certificates'
    certificates_folder = 'uploads'

    # Construct the full path to the certificate file
    full_certificate_path = os.path.join(certificates_folder, certificate_path)

    # Logic to check if the file exists before attempting to send it
    if os.path.exists(full_certificate_path):
        # Use send_from_directory to send the file
        return send_from_directory(certificates_folder, certificate_path, as_attachment=True)
    else:
        return "Certificate not found", 404


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # Save the uploaded file to the 'uploads' folder
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Process the Excel file and update the database or certificate files accordingly
            process_excel(file_path)

            flash('File uploaded successfully')
            return redirect(url_for('admin'))

    return render_template('admin.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_excel(file_path):
    # Read the Excel file and update the database or certificate files
    df = pd.read_excel(file_path)

    # Extract roll numbers and certificate file names from the DataFrame
    roll_numbers = df['Roll Number'].tolist()
    certificate_files = df['Certificate File'].tolist()

    # Your logic to update the database or certificate files based on the extracted data
    # ...

@app.route('/upload', methods=['POST'])
def upload_certificates():
    roll_number = request.form.get('rollNumber')

    # Check if the post request has the file part
    if 'certificateFiles' not in request.files:
        flash('No certificate files provided')
        return redirect(request.url)

    certificate_files = request.files.getlist('certificateFiles')

    # Iterate over the uploaded files
    for certificate_file in certificate_files:
        if certificate_file and allowed_file(certificate_file.filename):
            # Securely save the file to the UPLOAD_FOLDER
            filename = secure_filename(certificate_file.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], roll_number, filename)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            certificate_file.save(save_path)

    flash('Certificates uploaded successfully')
    return redirect(url_for('admin'))



if __name__ == '__main__':
    app.run(debug=True)
