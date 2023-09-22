# The goal is to create a mailing client
# Can NOT send emails directly from Python script
# If using gmail, you will need to activate 2-Step Authenicator 

import smtplib # Needed to connect to smtp server
from email import encoders #Base64,cnverts binary to plain characters
from email.mime.text import MIMEText  # Import for ordinary text being used
from email.mime.base import MIMEBase  # Used for the attachment 
from email.mime.multipart import MIMEMultipart # used to construct a message with varying content types.


# Variable- enter email provider with the port number
# Call function to start the process of connecting to server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
# add txt.file to avoid directly typing password in script 
# password will be in read mode
with open('password.txt', 'r') as file:
    password = file.read()
server.starttls()
server.ehlo()
server.login('networkmailtesting@gmail.com', password)
  

#Create a message a mail consisting of multiple messages and headers

msg = MIMEMultipart()
msg['From' ] = 'Violet'
msg['To'] = 'violetscreativeshowroom@gmail.com'
msg['Subject'] = 'IT Gives the Gateway to Endless Possiblities of Creativity'
# load the message from the message.txt in reading mode its added as a text not to the mail
with open('message.txt', 'r') as file:
    message = file.read()
# This is NOT the attachement this is adding a header with text with a message
msg.attach(MIMEText(message, 'plain'))


filename = 'VioletsCreative.jpg'
# the file is attached as reading binary(bites) since this is image data
attachement = open(filename, 'rb')
# octet-steam is a binary data format that is used to transfer files
# between different systems and to transfer files over the internet 
data = MIMEBase('apllication', 'octet-steam')
# Use of Payload
data.set_payload(attachement.read())
# This will break down the binary data into 6 bits segments of 3 full bytes
# Represents those as printable characters
encoders.encode_base64(data)
data.add_header('Content-Disposition', f'attachment; filename = {filename}')
msg.attach(data)

text = msg.as_string()
# Ok go ahead and send this to the mail server! 
server.sendmail('networkmailtesting@gmail.com', 'violetscreativeshowroom@gmail.com', text)
server.quit()


#Congradulations, you sent your first email using Python! Lets go ahead and add a print statement to confirm it sends!
print("Congradulations, you successfully sent your first email using Python!!!")