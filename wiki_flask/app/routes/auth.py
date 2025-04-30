from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app import db
from app.models import User
import requests

bp = Blueprint('auth', __name__)

RECAPTCHA_SECRET_KEY = 'your_secret_key_here'  # Replace with your actual secret key

def verify_recaptcha(recaptcha_response):
    payload = {
        'secret': RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
    }
    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
    result = response.json()
    return result.get('success')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        recaptcha_response = request.form['g-recaptcha-response']
        
        if not verify_recaptcha(recaptcha_response):
            flash('Please complete the CAPTCHA.')
            return redirect(url_for('auth.register'))

        hashed = generate_password_hash(password)
        user = User(username=username, password=hashed)
        db.session.add(user)
        db.session.commit()
        flash('ثبت‌نام موفقیت‌آمیز بود.')
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        recaptcha_response = request.form['g-recaptcha-response']
        
        if not verify_recaptcha(recaptcha_response):
            flash('Please complete the CAPTCHA.')
            return redirect(url_for('auth.login'))

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('articles.index'))
        flash('نام کاربری یا رمز عبور اشتباه است.')
    return render_template('login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))