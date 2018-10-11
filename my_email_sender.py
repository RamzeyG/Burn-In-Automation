import config
import os

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

def send_email(filename, to_email, from_email, subject, email_password, email_user):
    try:
        # Create the root message and fill in the from, to, and subject headers
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = subject
        msgRoot['From'] = from_email
        msgRoot['To'] = to_email
        msgRoot.preamble = 'This is a multi-part message in MIME format.'

        # Encapsulate the plain and HTML versions of the message body in an
        # 'alternative' part, so message agents can decide which they want to display.
        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        msgText = MIMEText('This is the alternative plain text message.')
        msgAlternative.attach(msgText)

        msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>Nifty!')
        msgAlternative.attach(msgText)

        # This example assumes the image is in the current directory
        fp = open('IV_logo.png', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        # Define the image's ID as referenced above
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)

        smtp = smtplib.SMTP()
        smtp.connect('smtp-mail.outlook.com', 587)
        smtp.starttls()
        smtp.login('rghanaim@intervision.com', '')
        smtp.sendmail('rghanaim@intervision.com', 'rghanaim@intervision.com', msgRoot.as_string())
        smtp.quit()

        # msg = MIMEMultipart()
        # msg['From'] = from_email
        # msg['To'] = to_email
        # msg['Subject'] = subject
        # body = 'Hi there, sending this email from Python! See the Attachment!'
        # msg.attach(MIMEText(body, 'plain'))
        #
        # attachment = open(filename, 'rb')
        #
        # part = MIMEBase('application', 'octet-stream')
        # part.set_payload((attachment).read())
        # encoders.encode_base64(part)
        # part.add_header('Content-Disposition', "attachment; filename= " + filename)
        #
        # msg.attach(part)
        # text = msg.as_string()
        # server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        # server.starttls()
        # server.login(email_user, email_password)
        #
        # server.sendmail(from_email, to_email, text)
        # server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")



def get_email_contents():
    body = '''<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><img src="cid:image1"></p>
<h1 style="text-align: center;"><strong><span style="color: #808080;">Intervision Compliance Report</span></strong></h1>
<p>&nbsp;</p>
<hr />
<p>&nbsp;</p>
<p>RE: Project</p>
<p>Hello, NAME,</p>
<p>&nbsp;</p>
<p>Your report can be seen attached. This is an automated e-mail.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>'''

    body2 = '<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>Nifty!'
    return body2

send_email(filename='pdf-sample.pdf', to_email=config.ME, from_email=config.ME,
           subject="Attachment2", email_password=config.PASSWORD, email_user=config.ME)



