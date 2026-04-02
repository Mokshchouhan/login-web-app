from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USER_FILE = "users.txt"

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Save to file
        with open(USER_FILE, 'a') as f:
            f.write(f"{username},{password}\n")

        return render_template("success.html", message="Registration Successful!", redirect_url="/login")

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            with open(USER_FILE, 'r') as f:
                users = f.readlines()
        except FileNotFoundError:
            return "No users registered yet!"

        for user in users:
            stored_username, stored_password = user.strip().split(',')

            if username == stored_username and password == stored_password:
                return render_template("success.html", message="Login Successful!", redirect_url="/login")

        return "Invalid Username or Password!"

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)