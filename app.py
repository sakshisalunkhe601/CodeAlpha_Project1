from flask import Flask, render_template, request
import string
import secrets

app = Flask(__name__)

def generate_password(length=12):
    # Combine all characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Securely pick random characters
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ""
    if request.method == 'POST':
        # Get length from form, default to 12 if not provided
        length = int(request.form.get('length', 12))
        password = generate_password(length)
    
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)