# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# مفتاح التشفير (تبديل الحروف الأبجدية)
key = {
    'a': 'Q', 'b': 'W', 'c': 'E', 'd': 'R', 'e': 'T',
    'f': 'Y', 'g': 'U', 'h': 'I', 'i': 'O', 'j': 'P',
    'k': 'A', 'l': 'S', 'm': 'D', 'n': 'F', 'o': 'G',
    'p': 'H', 'q': 'J', 'r': 'K', 's': 'L', 't': 'Z',
    'u': 'X', 'v': 'C', 'w': 'V', 'x': 'B', 'y': 'N',
    'z': 'M'
}

def monoalphabetic_encrypt(text):
    encrypted = ''
    for char in text.lower():
        if char in key:
            encrypted += key[char]
        else:
            encrypted += char
    return encrypted

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ''
    if request.method == 'POST':
        plaintext = request.form['text']
        result = monoalphabetic_encrypt(plaintext)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
