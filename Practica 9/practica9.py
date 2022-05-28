from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
import argparse

parser = argparse.ArgumentParser(description = 'Manda Multiples Correos')
args = parser.parse_args()

correo = args.a
message = args.m
correo = str(correo)
message = str(message)

data = {}
with open('C_User.json') as f:
        data = json.load(f)

# Creamos objeto Multipart
msg = MIMEMultipart()
message = "ALERTA DE SEGURIDAD!"
msg['From'] = data['user']

msg['To'] = julio14dan@gmail.com
msg['Subject'] = " FAVOR DE AUTENTICAR"

# Autenticamos
msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.office365.com:587')
server.starttls()
print(data['USER'])
server.login(data['USER'], data['PASSWORD'])

# Enviamos
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
print("successfully sent email to %s:" % (msg['To']))
