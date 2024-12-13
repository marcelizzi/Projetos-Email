import smtplib
from email.message import EmailMessage
import filetype
from time import sleep

class Emailer:
    def __init__(self,sender_email_address,email_password):
        self.sender_address = sender_email_address
        self.password = email_password
        
    def content(self,subject,sender_email,contacts,content):
        self.mail = EmailMessage()
        self.mail["Subject"] = subject
        message = content
        self.mail["From"] = sender_email
        self.mail["To"] = ", ".join(contacts)
        self.mail.add_header("Content-Type","text/html")
        self.mail.set_payload(message.encode("utf-8"))

    def attach_img(self,img_list):
        for image in img_list:
            with open(image,"rb") as image:
                data = image.read()
                img_extension = filetype.guess_extension(image)
                img_name = image.name
                self.mail.add_attachment(data, maintype="image", subtype=img_extension, filename=img_name)

    def attach_file(self,file_list):
        for file in file_list:
            with open(file, "rb") as file:
                data = file.read()
                file_name = file.name
                self.mail.add_attachment(data, maintype="application", subtype="octec-stream", filename=file_name)

    def send_email(self,delay):
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
            smtp.login(user=self.sender_address,password=self.password)
            smtp.send_message(self.mail)
            sleep(delay)