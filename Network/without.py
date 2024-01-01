import subprocess
import smtplib
from email.mime.text import MIMEText

def check_open_ports():

    target = '14.192.0.9'

    result = subprocess.run(['netstat', '-lnt'], capture_output=True, text=True)
    open_ports_info = result.stdout

    sender_email = 'dinakara.pathakota@gmail.com'
    sender_password = 'lqus scgq ipzr kekt'  

    recipient_email = 'dinakar.pathakota@gmail.com'


    subject = 'Open Ports Information'
    body = f'Open ports on {target}:\n\n{open_ports_info}'

    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())

if __name__ == "__main__":
    check_open_ports()

    import os
    if os.fork():
        os._exit(0)
