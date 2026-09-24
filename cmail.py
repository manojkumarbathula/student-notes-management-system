import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_mail(to, body, subject):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    server.login(
        os.environ.get("EMAIL_USER"),
        os.environ.get("EMAIL_PASSWORD")
    )

    msg = EmailMessage()
    msg["From"] = os.environ.get("EMAIL_USER")
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)

    server.send_message(msg)
    server.close()