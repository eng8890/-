@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted_text = ""
    plaintext = ""
    keymap = ""
    if request.method == 'POST':
        plaintext = request.form.get('plaintext', '')
        keymap = request.form.get('keymap', '')
        try:
            key_dict = parse_key_string(keymap)
            encrypted_text = mono_encrypt(plaintext, key_dict)
        except:
            encrypted_text = "Error in key format"
    else:
        key_dict = generate_key()
        keymap = key_to_string(key_dict)

    return render_template('index.html', encrypted=encrypted_text, keymap=keymap, plaintext=plaintext)
