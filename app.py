import smtplib
from email.message import EmailMessage

#Login Config
EMAIL_ADDRESS = "eng.marcelizzi@gmail.com"
EMAIL_PASSWORD = "kupy bpuc oadm ittm"

#Creating email
mail = EmailMessage()
mail["Subject"] = "Seu pacote chegou aos Correios"
message = """
Olá, sua encomenda está disponível para retirada na Agência dos Correios.
"""
mail["From"] = EMAIL_ADDRESS
mail["To"] = "marcelizzi@gmail.com"
mail.add_header("Content-Type","text/html")
mail.set_payload(message.encode("utf-8"))

#Sending email
with smtplib.SMTP_SSL("smtp.gmail.com",465) as email:
    email.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    email.send_message(mail)