import config
import os

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



# Create the root message and fill in the from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'test message'
msgRoot['From'] = 'rghanaim@intervision.com'
msgRoot['To'] = 'rghanaim@intervision.com'
msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('''Your recent project's burn in is complete''')
msgAlternative.attach(msgText)

name = "RAMZEY"
engineer = 'ramzey'

# We reference the image in the IMG SRC attribute by the ID we give it below
email_begin = '''<center><b> <p style="font-size:50px;"> Burn In Assessment Results</p> </b> <br><img src="cid:image1" 
width="40%" height="40%"><br></center>'''
email_middle = '''Hello, ''' + name + '\n\n'

email_end = '''<p>Attached you can find the burn in Assessment for your active project. Contact the Engineer: '''+engineer \
            + ''' if you have any questions.</p>

<p> This is an automated message. </p>'''

msgText = MIMEText(email_begin + email_middle + email_end, 'html')
msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
fp = open('IV_logo.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

# Send the email (this example assumes SMTP authentication is required)

smtp = smtplib.SMTP()
smtp.connect('smtp-mail.outlook.com', 587)
smtp.starttls()
smtp.login('rghanaim@intervision.com', 'Hellothere2')
smtp.sendmail('rghanaim@intervision.com', 'rghanaim@intervision.com', msgRoot.as_string())
smtp.quit()
