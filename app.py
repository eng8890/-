from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

# دالة لتوليد مفتاح تشفير عشوائي
def generate_key():
    alphabet = list(string.ascii_lowercase)
    shuffled_alphabet = alphabet[:]
    random.shuffle(shuffled_alphabet)
    return dict(zip(alphabet, shuffled_alphabet))

# دالة للتشفير باستخدام المفتاح
def encrypt_text(text, key):
    encrypted_text = ""
    for char in text.lower():
        if char in key:
            encrypted_text += key[char]
        else:
            encrypted_text += char  # الحفاظ على الأحرف غير الأبجدية كما هي
    return encrypted_text

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.json
        action = data.get("action")

        if action == "generate_key":
            key = generate_key()
            # إرسال المفتاح كسلسلة نصية بدلاً من JSON
            key_str = ", ".join([f"{k}: {v}" for k, v in key.items()])
            return jsonify({"key": key_str, "key_dict": key})

        elif action == "encrypt":
            text = data.get("text")
            key = data.get("key")  # يجب أن يكون المفتاح هنا قاموسًا
            encrypted_text = encrypt_text(text, key)
            return jsonify({"encrypted_text": encrypted_text})

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
