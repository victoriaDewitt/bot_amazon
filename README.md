
# 🤖 Bot de Disponibilidad de Productos en Amazon

Este proyecto es un bot escrito en Python que envía una alerta por correo electrónico cuando detecta disponibilidad de productos TCG (Trading Card Games) en Amazon México.  
Es ideal para automatizar la vigilancia de productos en tiendas en línea y recibir notificaciones en tiempo real.

---

## 🚀 Funcionalidades

- Conexión segura a una cuenta de Gmail mediante autenticación de aplicación.
- Envío de alertas por correo electrónico con contenido personalizado.
- Uso de variables de entorno para proteger credenciales.
- Estructura clara y adaptable para integrar un sistema de scraping.

---

## 🛠️ Tecnologías utilizadas

- Python 3.9+
- `smtplib` y `email.mime` para envío de correos
- `python-dotenv` para gestión de variables de entorno

---

## 📦 Instalación

1. **Clona este repositorio** en tu máquina local:

```bash
git clone https://github.com/tu_usuario/bot-amazon-tcg.git
cd bot-amazon-tcg
```

2. **Crea un entorno virtual (opcional, pero recomendado):**

```bash
python -m venv venv
venv\Scripts\activate  # En Windows
```

3. **Instala las dependencias:**

```bash
pip install -r requirements.txt
```

4. **Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:**

```env
EMAIL_USER=tu_correo@gmail.com
EMAIL_PASS=tu_contraseña_de_aplicación
```

⚠️ Para usar Gmail necesitas generar una **contraseña de aplicación** desde la configuración de seguridad de tu cuenta Google (necesitaras tener activada la verificación en dos pasos).

---

## ▶️ Uso

Una vez configurado el `.env`, solo ejecuta:

```bash
python monitor.py
```

Si todo está correcto, verás un mensaje de éxito en la terminal y recibirás un correo en tu bandeja de entrada.

---

## 🛡️ Seguridad

Este proyecto utiliza variables de entorno para proteger datos sensibles.  
Asegúrate de que el archivo `.env` **no sea subido** al repositorio público. Ya está incluido en `.gitignore`.

---

## 🧩 Ideas de mejora

- Agregar scraping real a Amazon con `requests` o `selenium`.
- Agregar más productos o categorías.
- Enviar alertas a Telegram, Discord o WhatsApp.
- Implementar interfaz web para configurar productos a monitorear.

---

## 📄 Licencia

Este proyecto está disponible bajo la licencia MIT. Puedes usarlo, modificarlo y adaptarlo libremente.
