import smtplib
import os
import ssl
import app




def email_buyer(email_add, first, last, item, price, seller, location, time, address, country, state, zipcode):
    PORT = 465  # For SSL. Have to use port 465 for gmail SSL
    password = os.environ.get("D6_PASSWORD")
    SENDER_EMAIL = "exchange4studentsd6@gmail.com"
    SUBJECT = "Exchange4Students Order Confirmation"
    RECEIVER_EMAIL = email_add
    # RECEIVER_EMAIL = order_info["email"]
    if(address is None):
        TEXT = f"""\n
            Subject: Order Confirmation\n
            
            Dear {first} {last},

            This is to confirm your purchase! 

            Below is your order information: 
            Item: {item}
            Price: {price}
            -----------------------------------------------------------
            Seller: {seller}
            Location: {location}
            Time: {time}
        

            

            -Exchange4Students
            """
            
    else:
        TEXT = f"""\n
        Subject: Order Confirmation\n
        
        Dear {first} {last},

        This is to confirm your purchase! 

        Below is your order information: 
        Item: {item}
        Price: {price}
        -------------------------------------------------------------
        Seller: {seller}
        Address: {address}
        State: {state}
        Zipcode: {zipcode}
        Country: {country}
        
    
        

        -Exchange4Students
        """

    MESSAGE = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
        server.login("exchange4studentsd6@gmail.com", password)
        # TODO: Send email here
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, MESSAGE)

def email_seller(seller, buyer_first, buyer_last, venmo, buyer_email, item, location,
 time, address, country, state, zipcode):
    PORT = 465  # For SSL. Have to use port 465 for gmail SSL
    password = os.environ.get("D6_PASSWORD")
    SENDER_EMAIL = "exchange4studentsd6@gmail.com"
    SUBJECT = "Exchange4Students Order Confirmation"
    RECEIVER_EMAIL = seller
    if(address is None):
        TEXT = f"""\n
            Subject: Order Confirmation\n
            
            Dear user,

            Someone bought your item!

            Below is the order information: 
            Item: {item}
            Buyer Name: {buyer_first} {buyer_last}    
            Email: {buyer_email}
            Venmo: {venmo}
            Location: {location}
            Time: {time}
            

            Sincerely, 

            Exchange4students

            """
    else:
        TEXT= f"""\n
          Subject: Order Confirmation\n
            
            Dear user,

            Someone bought your item!

            Below is the order information: 
            Item: {item}
            Buyer Name: {buyer_first} {buyer_last}    
            Email: {buyer_email}
            Venmo: {venmo}
            Address: {address}
            State: {state}
            Zipcode: {zipcode}
            Country: {country}
            

            Sincerely, 

            Exchange4students
            """
    MESSAGE = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server:
        server.login("exchange4studentsd6@gmail.com", password)
        # TODO: Send email here
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, MESSAGE)
