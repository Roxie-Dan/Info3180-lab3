import smtplib
from_addr = 'r.d.mowatt@gmail.com'
to_addr = 'r.m.danielle@hotmail.com'
message = """From: {} <{}>
To: {} <{}> 
Subject: {}
{}
"""
from_name = 'Roxann Mowatt'
to_name = 'Roxann Mowatt'
subject = 'Lab3'
msg = message
message_to_send = message.format(from_name, from_addr, to_name,
 to_addr, subject, msg)
# Credentials (if needed)
username = 'r.d.mowatt@gmail.com'
password = 'ayza cidi mbpe sysl'
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit() 