# 🤖 Amazon Product Availability Bot

This project is a Python bot that sends an email alert when a product becomes available on Amazon Mexico.  
It's ideal for automating product monitoring and receiving real-time notifications about restocks.


---

## 🚀 Features

- Secure connection to a Gmail account using app authentication.
- Email alerts with customizable content.
- Environment variables for credential protection.
- Clear and adaptable structure to integrate scraping logic.

---

## 🛠️ Technologies Used

- Python 3.9+
- `smtplib` and `email.mime` for email delivery
- `python-dotenv` for environment variable management

---

## 📦 Installation

1. **Clone this repository** to your local machine:

```bash
git clone https://github.com/your_username/amazon-product-availability-bot.git
cd amazon-product-availability-bot

```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. **Install the dependencies:**

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file** in the root directory of the project with the following content:


```env
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
```

⚠️ To use Gmail, you must generate an app password and have two-step verification enabled.
---

## ▶️ Usage

Once your `.env` file is properly configured, simply run:



```bash
python monitor.py
```

If everything is correct, you'll see a success message in the terminal and receive an email in your inbox.

---

## 🛡️ Security

This project uses environment variables to keep sensitive data safe.
Make sure your `.env` file **is not uploaded** to the public repository — it is already included in `.gitignore`.

---

## 🧩 Future Improvements

- Add real scraping functionality using `requests` or `selenium`.
- Support tracking multiple products or entire categories.
- Send alerts via Telegram, Discord, or WhatsApp.
- Create a web interface to manage monitored products.



---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
You are free to use, modify, and distribute it as you wish.

