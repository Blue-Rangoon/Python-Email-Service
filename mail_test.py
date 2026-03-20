import smtplib 

sender = "abc@gmail.com"
reciever = "xyz@gmail.com"
password = "abcd efgh ijkl mnop"
subject = "Python Email Test"

# three exclamatio marks for long string pattern in start and end
body = f"""Dear Recipient,

This email was sent automatically using a Python script as part of a demonstration of email automation using the SMTP protocol.

The purpose of this test is to verify that the Python-based email system is functioning correctly and can successfully deliver messages through an SMTP server.

Thank you for taking the time to review this demonstration.

Best regards,
@Blue-Rangoon on GitHub"""

#header
message = f"""from: ABC {sender}
To: XYZ {reciever}
Subject: {subject}\n

{body}
"""

#server 

server = smtplib.SMTP("smtp.gmail.com", 587) #default port number 587 for mail submission
server.starttls()   #object

#catch errors
try: 
    server.login(sender, password)
    print("Logged In...")

    #send email
    server.sendmail(sender, reciever, message)
    print("Email has been sent...")

except smtplib.SMTPAuthenticationError:
    print("Unable to Sign in! Please try again later...")