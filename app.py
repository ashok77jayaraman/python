from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Add your authentication logic here
    # For simplicity, let's check for a hardcoded username and password
    if username == 'user' and password == 'password':
        return f'Welcome, {username}!'
    else:
        return 'Invalid username or password'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

