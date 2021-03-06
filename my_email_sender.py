import config
import os

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

def send_email(filename, to, to_email, sender, subject):
    try:
        # Create the root message and fill in the from, to, and subject headers
        print sender
        print to
        print to_email
        engineer = sender[0]
        from_email = sender[1]
        email_password = sender[2]



        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = subject
        msgRoot['From'] = from_email
        msgRoot['To'] = ", ".join(to_email)
        msgRoot.preamble = 'This is a multi-part message in MIME format.'

        # Encapsulate the plain and HTML versions of the message body in an
        # 'alternative' part, so message agents can decide which they want to display.
        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        msgText = MIMEText('''Your recent project's burn in is complete''')
        msgAlternative.attach(msgText)

        # We reference the image in the IMG SRC attribute by the ID we give it below
        email_begin = '''
        <head>
  <style>
  * {
   margin: 0;
   padding: 0;
  }
  .imgbox {
   display: grid;
   height: 100%;
  }
  .center-fit {
   max-width: 100%;
   max-height: 100vh;
   margin: auto;
  }
  </style>
 </head>
        <center><b> <p style="font-size:50px;"> Burn In Results</p> </b> <br><img class="center-fit" src="cid:image1">
        <br></center> <hr>'''
        email_middle = '''\n\nHello ''' + ", ".join(to) + ',\n\n'

        email_end = '''<p>Attached you can find the burn in assessment for your active project. Contact the Engineer: ''' + engineer \
                    + ''' if you have any questions.</p>

        <p> This is an automated message Brought to you by a new automation initiative at InterVision. </p>'''

        msgText = MIMEText(email_begin + email_middle + email_end, 'html')
        msgAlternative.attach(msgText)

        # This example assumes the image is in the current directory
        fp = open('IV_logo.png', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        # Define the image's ID as referenced above
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)


        # Email attachment
        for file in filename:
            print 'file is ', file
            attachment = open(file, 'rb')

            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= " + file)

            msgRoot.attach(part)

        # Send e-mail
        smtp = smtplib.SMTP()
        smtp.connect('smtp-mail.outlook.com', 587)
        smtp.starttls()
        email_user = from_email
        smtp.login(email_user, email_password) # Returns type tuple
        smtp.sendmail(from_email, to_email, msgRoot.as_string())
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
    body = '''<p style="text-align: center;">&nbsp;</p>'''
    return body2

# name = []
# name.append('burn-in-results-016201004695.pdf')
# name.append('burn-in-results-016201004696.pdf')
# name.append('burn-in-results-016201004721.pdf')
# name.append('burn-in-results-016201004725.pdf')
#
# me = []
# me.append('Ramzey Ghanaim')
# me.append('rghanaim@intervision.com')
# me.append('')
#
# to = []
# to.append('Jon Greco')
# to.append('jgreco@intervision.com')
#
# send_email(filename=name, subject="Burn In Results", to=to, sender=me)
#


