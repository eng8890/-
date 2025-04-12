from flask import Flask, render_template, request
import os

app = Flask(__name__)

# دالة تشفير monoalphabetic
def mono_encrypt(text, key_map):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += key_map.get(char, char)
            else:
                result += key_map.get(char.lower(), char).upper()
        else:
            result += char
    return result

# خارطة التشفير: كل حرف مقابل له حرف آخر (تقدر تغيرها)
default_key = {
    'a': 'm', 'b': 'n', 'c': 'b', 'd': 'v', 'e': 'c',
    'f': 'x', 'g': 'z', 'h': 'l', 'i': 'k', 'j': 'j',
    'k': 'h', 'l': 'g', 'm': 'f', 'n': 'd', 'o': 's',
    'p': 'a', 'q': 'p', 'r': 'o', 's': 'i', 't': 'u',
    'u': 'y', 'v': 't', 'w': 'r', 'x': 'e', 'y': 'w',
    'z': 'q'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted_text = ""
    if request.method == 'POST':
        text = request.form['plaintext']
        encrypted_text = mono_encrypt(text, default_key)
    return render_template('index.html', encrypted=encrypted_text)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
