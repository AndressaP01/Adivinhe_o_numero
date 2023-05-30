import os
import smtplib
from email.message import EmailMessage

Email_Address="testecigithubactions@gmail.com"
senha="esmkzovbpounaoez"

msg=EmailMessage()
msg['Subject']="Pipeline"
msg['From']="testecigithubactions@gmail.com"
msg['To']="testecigithubactions@gmail.com"
msg.set_content("Pipeline executado")

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(Email_Address,senha)
    smtp.send_message(msg)
