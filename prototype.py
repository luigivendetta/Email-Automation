# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 13:20:46 2020

@author: Ayush
"""


# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 20:41:07 2020

@author: Ayush
"""


# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 21:21:22 2020

@author: Ayush
"""


#to create pdf report
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
#to automate email
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication


# assign key email aspects to variables for easier future editing
subject = "Weekly Report"
body = "This is an email with the desired report attached"
#sender_email = "tech@entrepreneurshipnetwork.net"
#receiver_email = "ayush.core123@gmail.com"
file = "em.py"
img_file = "got.jpg" # in the same directory as script
pdf_file = "Ayush Srivastava Resume.pdf"
#password = "Tn(oA(V1"
sender_email = input("Enter your e-mail: ")
service = (sender_email.split("@")[1]).split(".")[0]
password = input("Enter password: ")
receiver_email = input("Enter receiever's e-mail: ")

# Create the email head (sender, receiver, and subject)
email = MIMEMultipart()
email["From"] = sender_email
email["To"] = receiver_email 
email["Subject"] = subject
# Add body and attachment to email
email.attach(MIMEText(body, "plain"))
attach_file = open(file, "rt") # open the file
img_data = open(img_file, "rb")
pdf_data = open(pdf_file, "rb")
report = MIMEBase("application", "octet-stream", name = file)
pdf = MIMEBase("text", "octet_stream", name= pdf_file)
pdf.set_payload((pdf_data).read())
report.set_payload((attach_file).read())
image = MIMEBase("image", "octet-stream", name = img_file)
#email.attach(image)
image.set_payload((img_data).read())
#email.attach(pdf)
encoders.encode_base64(report)
encoders.encode_base64(image)
encoders.encode_base64(pdf)
#add report header with the file name
#report.add_header("Content-Decomposition", "attachment", filename = file)
email.attach(report)
email.attach(image)
email.attach(pdf)
#Create SMTP session for sending the mail

if service == "gmail":
    #use gmail with port
    session = smtplib.SMTP('smtp.gmail.com', 587)
if service == "entrepreneurshipnetwork":
    session = smtplib.SMTP('smtp.entrepreneurshipnetwork.net', 587)
if service == "hotmail" or service == "outlook":
    session = smtplib.SMTP("smtp.outlook.com", 587)
session.starttls() #enable security 
session.login(sender_email, password) #login with mail_id and password
text = email.as_string()
session.sendmail(sender_email, receiver_email, text)
print('Mail Sent')
session.quit()



    