from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import check_password_hash
from flask_login import (
    login_user,
    login_required,
    logout_user,
    current_user,
)


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')

        password = request.form.get('password')

        user = User.query.filter_by(login=login).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)

                return redirect(url_for('views.home'))
            else:
                flash('Не получилось выполнить авторизацию...', category='error')
        else:
            flash('Не получилось выполнить авторизацию...', category='error')

    return render_template('login.html', current_user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for('auth.login'))
