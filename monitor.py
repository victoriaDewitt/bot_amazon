# monitor.py
# URL del producto a monitorear (personaliza esta línea con tu producto)
product_url = "https://www.amazon.com.mx/dp/ID_DEL_PRODUCTO"

from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText

# Cargar variables de entorno desde .env
load_dotenv()
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def enviar_correo():
    subject = "📦 Alerta de disponibilidad de producto"
    body = "Este es un correo automático generado por el bot de disponibilidad."

    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_USER

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASS)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    print("✅ Correo enviado correctamente.")

# Ejecutar
if __name__ == "__main__":
    enviar_correo()
