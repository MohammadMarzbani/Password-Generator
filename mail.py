import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PasswordGT import passwordlist

def send_smtp_email(subject, body):
    smtp_server = "mail.phpself.ir"
    smtp_port = 465
    username = "mail@phpself.ir"
    password = "$@viorking"

    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = passwordlist['Gmail']
    msg['Subject'] = subject

    body = body
    msg.attach(MIMEText(body, 'plain'))
    server = None
    try:

        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(username, password)
        server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        if server is not None:
            server.quit()
