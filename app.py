from flask import Flask, render_template, request
import os
import random
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'

# دالة توليد مفتاح تشفير عشوائي
def generate_random_key():
    letters = list(string.ascii_lowercase)
    shuffled = letters[:]
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled))

# تحويل سلسلة مفتاح (string) إلى dict
def parse_key_string(key_str):
    key_map = {}
    pairs = key_str.lower().split(',')
    for pair in pairs:
        if ':' in pair:
            k, v = pair.split(':')
            key_map[k.strip()] = v.strip()
    return key_map

# دالة التشفير
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
    user_key_str = ""
    plaintext = ""
    generated_key = generate_random_key()
    default_key_str = ', '.join([f"{k}:{v}" for k, v in generated_key.items()])

    if request.method == 'POST':
        plaintext = request.form.get('plaintext', '')
        user_key_str = request.form.get('keymap', default_key_str)
        try:
            key_map = parse_key_string(user_key_str)
            encrypted_text = mono_encrypt(plaintext, key_map)
        except Exception as e:
            encrypted_text = f"Error in key format: {e}"
    
    return render_template('index.html', encrypted=encrypted_text, keymap=user_key_str, plaintext=plaintext)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
