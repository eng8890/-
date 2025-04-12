from flask import Flask, render_template, request
import random
import string
import os

app = Flask(__name__)

def generate_key():
    letters = list(string.ascii_lowercase)
    shuffled = letters[:]
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled))

def key_to_string(key_dict):
    return ', '.join([f"{k}:{v}" for k, v in key_dict.items()])

def parse_key_string(key_str):
    key_map = {}
    pairs = key_str.lower().split(',')
    for pair in pairs:
        if ':' in pair:
            k, v = pair.split(':')
            key_map[k.strip()] = v.strip()
    return key_map

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

@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted_text = ""
    plaintext = ""
    if request.method == 'POST':
        plaintext = request.form.get('plaintext', '')
        keymap = request.form.get('keymap', '')
        try:
            key_dict = parse_key_string(keymap)
            encrypted_text = mono_encrypt(plaintext, key_dict)
        except:
            encrypted_text = "Error in key format"
        return render_template('index.html', encrypted=encrypted_text, keymap=keymap, plaintext=plaintext)
    else:
        key_dict = generate_key()
        keymap = key_to_string(key_dict)
        return render_template('index.html', encrypted="", keymap=keymap, plaintext="")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
