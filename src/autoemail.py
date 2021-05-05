import smtplib
import os
import ssl
from app import order_info_dict

order_info = order_info_dict

PORT = 465  # For SSL. Have to use port 465 for gmail SSL
password = os.environ.get("D6_PASSWORD")
SENDER_EMAIL = "exchange4studentsd6@gmail.com"
SUBJECT = "Exchange4Students Order Confirmation"
RECEIVER_EMAIL = order_info["email"]
TEXT = f"""\n
    Subject: Order Confirmation\n
    
    Dear {order_info["first"]} {order_info["last"]},

    This is to confirm your purchase! 

    Below is your order information: 

    Item: {order_info["item_name"]}
     

    -Grace

    """

MESSAGE = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
    server.login("exchange4studentsd6@gmail.com", password)
    # TODO: Send email here
    server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, MESSAGE)
