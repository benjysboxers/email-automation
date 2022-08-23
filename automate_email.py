import smtplib #SMTP client session object to send mail to any internet mahine with an SMTP or ESMTP 
import ssl #encryption and peer authentication facilities for network sockets, both client and server side
from email.message import EmailMessage

email_sender ='' # the gmail sending the mail
email_pass = '' # 16 character password you generated goes in here
email_receiver = '' # the person recieving the gmail (you can't test it with an alt gmail or your friends if you want)

subject = 'Testing sending emails using python'
body = """
Trying to do something with my braincells.exe
please don't laugh about it.
"""                                         # content you wish to send across goes in here 

em = EmailMessage()

#passing our assigned variables from before into a formated structure 
em['From'] = email_sender 
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body) #basically a structured format as seen in the gmail when you usually compose something to send 

context = ssl.create_default_context() # used for security and safeguarding any sensitive data that is sent between two systems

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_pass)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
