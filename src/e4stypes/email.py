import smtplib

smtpObj = smtplib.SMTP('localhost') #this makes the SMTP object that runs the SMTP server.

sender = "exchange4studentsd6@gmail.com"
receiver = ['gracem730@gmail.com']

message = f"""From: <{sender}>
To: <{receiver[0]}>
Subject: SMTP e-mail test

This is a test email message.
 """

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receiver, message)
    print("Successfully sent email")
