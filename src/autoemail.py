import smtplib
import os
import ssl

port = 465  # For SSL. Have to use port 465 for gmail SSL
password = os.environ.get("D6_PASSWORD")
sender_email = "exchange4studentsd6@gmail.com"
receiver_email = "gracem730@gmail.com"
message = """\n 
    Subject: Test Email\n
    

    This is from Exchange4students. Time to figure out automation

    -Grace

    """


# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("exchange4studentsd6@gmail.com", password)
    # TODO: Send email here
    server.sendmail(sender_email, receiver_email, message)
