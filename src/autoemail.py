import smtplib
import os
import ssl

PORT = 465  # For SSL. Have to use port 465 for gmail SSL
password = os.environ.get("D6_PASSWORD")
SENDER_EMAIL = "exchange4studentsd6@gmail.com"
RECEIVER_EMAIL = "gracem730@gmail.com"
MESSAGE = """\n
    Subject: Test Email\n
    

    This is from Exchange4students. Time to figure out automation

    -Grace

    """


# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
    server.login("exchange4studentsd6@gmail.com", password)
    # TODO: Send email here
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, MESSAGE)
