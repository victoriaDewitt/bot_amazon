# monitor.py
# URL of the product to monitor (customize this line with your own product)
product_url = "https://www.amazon.com.mx/dp/PRODUCT_ID"

from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText

# Load environment variables from .env
load_dotenv()
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def send_email():
    subject = "📦 Product Availability Alert"
    body = "This is an automated email sent by the availability bot."

    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_USER

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASS)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    print("✅ Email sent successfully.")

# Run the bot
if __name__ == "__main__":
    send_email()
