from flask import Flask, render_template, redirect, url_for, Blueprint
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/index')
def redirect_back():
    return redirect(url_for('index'))


@main.route('/user')
@login_required
def user():
    return render_template('profile.html', name=current_user.name)


@main.route('/map')
@login_required
def map():
    return render_template('user.html', name=current_user.name)


@main.route('/driver')
def driver():
    return render_template('driver.html')
