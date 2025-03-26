
This program  is stored in folder

/var/www/10/zenlukkari/sites/sandy.dysfapsia.us/www/python
name of program: send_email_att11.py

import smtplib
from email.message import EmailMessage
from pathlib import Path
import os
from os import environ as env


dirpath="/var/log/www_logs/sandy.dysfapsia.us"
print(dirpath)


receiver_email = os.environ.get('EMAIL_RECEIVER1')
sender_email = os.environ.get('EMAIL_SENDER1')
email_password = os.environ.get('EMAIL_PASSWORD1')

body=""" line  """
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "sending mail using python"
#message.set_content(body, 'plain')


# The OS will look in the current working directory, not in the directory where you saved the script
filename= os.path.join(dirpath, "access.log")
print(filename)
# 


with open(filename, 'rb') as attachment:
    
    message.add_attachment(
        attachment.read(),
        maintype='text', subtype='plain/txt')

#  default SSL
with smtplib.SMTP_SSL('mail.kapsi.fi', 465) as server:
    server.login(sender_email, email_password)
    # 
    server.send_message(message)
    
    
    
