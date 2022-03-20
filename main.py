from flask import Flask, render_template, redirect, url_for, Blueprint, request
from flask_login import login_required, current_user
import requests
from .Map_Nodes import init

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


@main.route('/new_booking', methods=['POST'])
@login_required
def new_booking():
    from_Loc = request.form['fromLoc']
    to_Loc = request.form['toLoc']
    g, overview = init()
    return_val = []
    for k,v in overview.items():
        if from_Loc in v or to_Loc in v:
            return_val.append(v)
    return render_template('booked.html', name=current_user.name, test=return_val)


@main.route('/booking')
@login_required
def booking():
    g, overview = init()
    return_val = []
    for k,v in overview.items():
        return_val.append(v)
    return render_template('booking.html', name=current_user.name, map_var=return_val)


@main.route('/display_map')
@login_required
def display_map():
    g, overview = init()
    return_val = []
    for k,v in overview.items():
        return_val.append(v)
    return render_template('map.html', map_vars=return_val)


@main.route('/driver')
def driver():
    return render_template('driver.html')
