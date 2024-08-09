from flask import render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from . import auth

login_manager = LoginManager()

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Dummy user store
USERS = {"admin@gmail.com": {"password": "adminpass"}}

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email_services']
        password = request.form['password']
        if email in USERS and USERS[email]['password'] == password:
            user = User(email)
            login_user(user)
            return redirect(url_for('main.scan_qr'))
        else:
            flash('Invalid email_services or password')
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
