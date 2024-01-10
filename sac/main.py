import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(roll_number, recipient_email):
    # Email configuration
    sender_email = 'sac@klh.edu.in'
    sender_password = 'qnve lqsx puxn hkur'
    subject = 'SIL2 Certificate'
    body = f'Dear {roll_number},\n\nPlease find the attached PDF file, which is the Certificate for SIL2 Activity.\n\nBest regards,\nSAC,\nKLH University'

    # Create a MIME multipart message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    # Attach the PDF file
    pdf_filename = f'{roll_number}.pdf'
    with open(pdf_filename, 'rb') as pdf_file:
        pdf_attachment = MIMEApplication(pdf_file.read(), _subtype="pdf")
        pdf_attachment.add_header('Content-Disposition', f'attachment; filename={pdf_filename}')
        message.attach(pdf_attachment)

    # Connect to the SMTP server (in this case, Gmail's SMTPz server)
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())

if __name__ == "__main__":
    # Read roll numbers from an Excel sheet
    excel_file = './FRC CSEA.xlsx'  # Replace with the actual path to your Excel file
    df = pd.read_excel(excel_file)

    for index, row in df.iterrows():
        roll_number_to_send = str(row['UNIVERSITY ID'])
        recipient_email_address = roll_number_to_send + '@klh.edu.in'
        try:
            send_email(roll_number_to_send, recipient_email_address)
            print(f'Email sent successfully to {recipient_email_address} for roll number {roll_number_to_send}.')
        except Exception as e:
            print(f'Error: {e}')
