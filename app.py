from flask import Flask, render_template, request, jsonify
from cryptography.fernet import Fernet
import os

app = Flask(__name__)

# Key management for Fernet
if not os.path.exists("secret.key"):
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
else:
    with open("secret.key", "rb") as key_file:
        key = key_file.read()

fernet_cipher = Fernet(key)

# Caesar Cipher functions
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    method = data['method']
    message = data['message']

    if method == 'Fernet':
        encrypted = fernet_cipher.encrypt(message.encode()).decode()
        decrypted = fernet_cipher.decrypt(encrypted.encode()).decode()
        return jsonify({'encrypted': encrypted, 'decrypted': decrypted})

    elif method == 'Caesar':
        shift = int(data.get('shift', 3))
        encrypted = caesar_encrypt(message, shift)
        decrypted = caesar_decrypt(encrypted, shift)
        return jsonify({'encrypted': encrypted, 'decrypted': decrypted})

    return jsonify({'error': 'Invalid method'}), 400

if __name__ == '__main__':
    app.run(debug=True)
