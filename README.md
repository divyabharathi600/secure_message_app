# secure_message_app


```markdown
# 🔐 Secure Messaging Web App using Fernet and Caesar Cipher

A Flask-based secure messaging web application that allows users to encrypt and decrypt messages using **Fernet Encryption** and the **Caesar Cipher**.

> 💡 Choose between **strong encryption (Fernet)** or **classical learning cipher (Caesar)** to secure your messages in a stylish, interactive web interface.

---

## 📸 Demo Screenshots
<img width="1911" height="962" alt="Screenshot 2025-07-29 124103" src="https://github.com/user-attachments/assets/4687dd85-fd94-4b36-b1fc-12a31b868f36" />


---

## ✨ Features

- 🔐 **Fernet Encryption**
  - AES + HMAC + base64
  - Secure, production-level encryption
- 🧠 **Caesar Cipher**
  - Simple character shifting
  - Great for educational use
- 🖥️ **Responsive Web UI**
  - Clean, animated interface
  - Glassmorphism style
- 🔄 Real-time AJAX encryption
- 📜 Displays both encrypted and decrypted messages

---

## 📁 Project Structure

```

secure\_messaging\_app/
├── app.py                # Flask backend
├── secret.key            # Fernet key file (auto-generated)
├── templates/
│   └── index.html        # UI Template
├── static/
│   ├── style.css         # Stylish CSS
│   └── script.js         # JavaScript for interactivity
└── README.md

````

---

## 🚀 Getting Started

### 📦 Prerequisites

- Python 3.x
- pip (Python package installer)

### 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/secure-messaging-app.git
   cd secure-messaging-app
````

2. Install dependencies:

   ```bash
   pip install flask cryptography
   ```

3. Run the app:

   ```bash
   python app.py
   ```

4. Open in browser:

   ```
   http://127.0.0.1:5000
   ```

---

## 🧪 How It Works

### Fernet

* Encrypts using AES in CBC mode with a random key
* Base64 encoded output for safe display
* Requires the same key for decryption

### Caesar

* Shifts letters based on a numeric value
* Preserves spaces, punctuation
* Great for demonstrating classical ciphers

---

## 📚 Learn More

* [Cryptography Docs – Fernet](https://cryptography.io/en/latest/fernet/)
* [Wikipedia – Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
* [Flask Documentation](https://flask.palletsprojects.com/)

---


