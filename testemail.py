# YouTube Video: https://www.youtube.com/watch?v=mP_Ln-Z9-XY
import smtplib

import config


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.TO_EMAIL_ADDRESS, config.TO_EMAIL_ADDRESS, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = "I wasn't joking..."
msg = "Let the e-mail spam begin!...Let me know if this works. \n Automated by Ramzey"

send_email(subject, msg)
