# learn how to do this here:
# https://www.youtube.com/watch?v=YPiHBtddefI

# go here to turn on less secure apps:
# https://myaccount.google.com/lesssecureapps?pli=1

import smtplib

email = 'stevenrobinson48291@gmail.com' # Your email
password = '...' # Your email account password
send_to_email = 'mathewdblewis@gmail.com' # Who you are sending the message to
message = 'This is my message' # The message in the email

server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
server.starttls() # Use TLS
server.login(email, password) # Login to the email server
server.sendmail(email, send_to_email , message) # Send the email
server.quit() # Logout of the email server


