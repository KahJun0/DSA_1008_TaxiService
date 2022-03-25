from flask import Flask, render_template, redirect, url_for, Blueprint, request
from flask_login import login_required, current_user
from .Graph import Graph
from .MatchingSystem import Record, Driver, Passenger

main = Blueprint('main', __name__)
db = Record()


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
    overview = Graph.overview
    from_node = -1
    to_node = -1
    i = 0
    for k, v in overview.items():
        if from_Loc not in v and to_Loc not in v:
            i += 1
        elif from_Loc in v:
            from_node = i
            i += 1
        elif to_Loc in v:
            to_node = i
            i += 1
    add_passenger = Passenger(current_user.id, current_user.name)
    match = add_passenger.requestRide(db, from_node, to_node)
    node_list = add_passenger.visitingNodes
    return_val = []
    for i in node_list:
        return_val.append(overview[i])
    return render_template('booked.html', name=current_user.name, match=match, return_val=return_val)


@main.route('/new_driver', methods=['POST'])
@login_required
def new_driver():
    start_loc = request.form['startLoc']
    end_loc = request.form['endLoc']
    overview = Graph.overview
    add_driver = Driver(current_user.name, current_user.name)
    start_node = -1
    end_node = -1
    i = 0
    for k, v in overview.items():
        if start_loc not in v and end_loc not in v:
            i += 1
        elif start_loc in v:
            start_node = i
            i += 1
        elif end_loc in v:
            end_node = i
            i += 1
    add_driver.offerRide(db, start_node, end_node, 99)
    return render_template('booked.html', name=current_user.name, start=[[start_loc, start_node], [end_loc, end_node]])


@main.route('/booked')
@login_required
def booked():
    if current_user.membership == 0:
        list_drivers = db.drivers
        for i in db.drivers:
            if i.name == current_user.name:
                return render_template('booked.html', name=current_user.name, status_driver=[i.starting, i.destination])


@main.route('/booking')
@login_required
def booking():
    overview = Graph.overview
    return_val = []
    for k, v in overview.items():
        return_val.append(v)
    if current_user.membership == 0:  # driver:
        return render_template('driver.html', name=current_user.name, map_var=return_val,
                               membership=current_user.membership)
    else:
        return render_template('booking.html', name=current_user.name, map_var=return_val,
                               membership=current_user.membership)


@main.route('/display_map')
@login_required
def display_map():
    overview = Graph.overview()
    return_val = []
    for k, v in overview.items():
        return_val.append(v)
    return render_template('map.html', map_vars=return_val)


@main.route('/driver')
def driver():
    return render_template('driver.html')
