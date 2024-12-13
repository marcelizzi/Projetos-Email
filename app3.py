import smtplib
from email.message import EmailMessage
import filetype

#Login Config
EMAIL_ADDRESS = "eng.marcelizzi@gmail.com"
EMAIL_PASSWORD = "kupy bpuc oadm ittm"

#Creating email
mail = EmailMessage()
mail["Subject"] = "Seu pacote chegou"
message = """
Os anexos chegaram.
"""
mail["From"] = EMAIL_ADDRESS
mail["To"] = "marcelizzi@gmail.com"
mail.add_header("Content-Type","text/html")
mail.set_payload(message.encode("utf-8"))

#Attaching images
images = ["bluesky.jpg","retro.jpg"]
for image in images:
    with open(image,"rb") as image:
        data = image.read()
        img_extension = filetype.guess_extension(image)
        img_name = image.name
        mail.add_attachment(data, maintype="image", subtype=img_extension, filename=img_name)

#Attaching other files
files = ["csv_exemplo.csv","exemplo_word.docx","ExemploPlanilha.xlsx","PDF_Exemplo.pdf","templatehtml.html","Untitled presentation.pptx"]
for file in files:
    with open(file, "rb") as file:
        data = file.read()
        file_name = file.name
        mail.add_attachment(data, maintype="application", subtype="octec-stream", filename=file_name)

#Sending email
with smtplib.SMTP_SSL("smtp.gmail.com",465) as email:
    email.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    email.send_message(mail)