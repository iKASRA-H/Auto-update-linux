import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
os.system('sudo apt update')
os.system('sudo apt -y upgrade')
mail_content = '''Hi boss, I have updated your server!'''
#The mail addresses and password
sender_address = 'your gmail'
sender_pass = 'your gmail password'
receiver_address = 'the mail that you want to recieve the notice'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Server Guard: Update Notice'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
os.system('sudo reboot')
