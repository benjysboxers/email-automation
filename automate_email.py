import smtplib #SMTP client session object to send mail to any internet mahine with an SMTP or ESMTP 
import ssl #encryption and peer authentication facilities for network sockets, both client and server side
from email.message import EmailMessage

email_sender ='good435lovesyou@gmail.com'
email_pass = 'denvlnyrbwnfodbf'
email_receiver = 'pfidowu@gmail.com'

subject = 'Testing sending emails using python'
body = """
Trying to do something with my braincells.exe
please don't laugh about it.
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context() # used for security and safeguarding any sensitive data that is sent between two systems

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_pass)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
