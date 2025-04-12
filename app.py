from flask import Flask, render_template, request, redirect, url_for
import random
import string

app = Flask(__name__)

def generate_keymap():
    letters = list(string.ascii_lowercase)
    shuffled = letters[:]
    random.shuffle(shuffled)
    return ', '.join(f"{a}:{b}" for a, b in zip(letters, shuffled))

def encrypt(text, keymap):
    mapping = {}
    for pair in keymap.split(','):
        if ':' in pair:
            k, v = pair.strip().split(':')
            mapping[k.strip()] = v.strip()

    result = ""
    for char in text:
        lower_char = char.lower()
        if lower_char in mapping:
            enc_char = mapping[lower_char]
            result += enc_char.upper() if char.isupper() else enc_char
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    keymap = generate_keymap()
    encrypted = ''
    plaintext = ''

    if request.method == 'POST':
        plaintext = request.form['plaintext']
        keymap = request.form['keymap']
        encrypted = encrypt(plaintext, keymap)

    return render_template('index.html', encrypted=encrypted, plaintext=plaintext, keymap=keymap)

@app.route('/generate-key')
def generate_key():
    keymap = generate_keymap()
    return redirect(url_for('index', keymap=keymap))

if __name__ == '__main__':
    app.run(debug=True)
