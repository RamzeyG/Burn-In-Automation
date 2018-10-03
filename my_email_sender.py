import config
import os

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(filename, to_email, from_email, subject, email_password, email_user):
    try:
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        body = 'Hi there, sending this email from Python! See the Attachment!'
        msg.attach(MIMEText(body, 'plain'))

        attachment = open(filename, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= " + filename)

        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(email_user, email_password)

        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")



# send_email(filename='pdf-sample.pdf', to_email=config.EMAIL_ADDRESS, from_email=config.EMAIL_ADDRESS,
#          subject="Attachment2", email_password=config.PASSWORD, email_user=config.EMAIL_ADDRESS)
