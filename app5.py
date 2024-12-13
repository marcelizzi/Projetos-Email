from email_sender import Emailer

email = Emailer("eng.marcelizzi@gmail.com","kupy bpuc oadm ittm")

lista_de_contatos = ["marcelizzi@gmail.com","prof.marcelizzi@gmail.com","eng.marcelizzi@gmail.com"]

mensagem = """
Olá, obrigado por comprar nosso curso.
"""

email.content(subject="Bem vindo",sender_email="eng.marcelizzi@gmail.com",contacts=lista_de_contatos,content=mensagem)

lista_imagens = ["bluesky.jpg","retro.jpg"]
email.attach_img(lista_imagens)

lista_arquivos = ["csv_exemplo.csv","exemplo_word.docx","ExemploPlanilha.xlsx","PDF_Exemplo.pdf","templatehtml.html","Untitled presentation.pptx"]
email.attach_file(lista_arquivos)

email.send_email(25)