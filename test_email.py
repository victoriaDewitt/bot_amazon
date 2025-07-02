import smtplib
from email.mime.text import MIMEText

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('vazquezgtz2204@gmail.com', 'ypqkrdauaawxgytl')

subject = "🧪 Prueba de correo del bot TCG"
body = "¡Hola Vicky! Este es un correo de prueba desde tu bot de Amazon."

# Crear el mensaje MIME con codificación UTF-8
msg = MIMEText(body, 'plain', 'utf-8')
msg['Subject'] = subject
msg['From'] = 'vazquezgtz2204@gmail.com'
msg['To'] = 'vazquezgtz2204@gmail.com'

# Enviar el correo usando msg.as_string()
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print("✅ Correo de prueba enviado correctamente.")
