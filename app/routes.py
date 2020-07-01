from datetime import datetime

from flask import render_template, flash, redirect, url_for, request, jsonify, abort
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app, db, images
from app.models import User, Plant, Watering
from app.forms import LoginForm, PlantRegistrationForm, PlantWateringForm

@app.route('/')
@app.route('/index')
def index():
    plants = Plant.query.order_by("name").all()
    return render_template('index.html', title='The Constant Gardener', plants=plants)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password') 
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register_plant', methods=['GET', 'POST'])
@login_required
def register_plant():
    form = PlantRegistrationForm()
    if form.validate_on_submit():
        last_watered_datetime = datetime.combine(form.last_watered_date.data, form.last_watered_time.data)
        
        filename = images.save(request.files['photo'])
        url = images.url(filename)

        plant = Plant(name=form.name.data, location=form.location.data, last_watered=last_watered_datetime, image_filename=filename, image_url=url)

        db.session.add(plant)
        db.session.commit()
        flash('Congratulations, new plant registered')
        return redirect(url_for('index'))
    return render_template('register_plant.html', title='Register Plant', form=form)

@app.route('/water_plants', methods=['GET', 'POST'])
@login_required
def water_plants():
    form = PlantWateringForm()
    if form.validate_on_submit():

        for plant in form.plants_to_water.data:
            p = Plant.query.filter_by(name=plant).first()
            p.last_watered = datetime.utcnow()
            db.session.commit()
        
        flash('Congratulations, last watered time for plant(s): ' + ','.join(form.plants_to_water.data) + ' recorded')
        return redirect(url_for('index'))
    return render_template('water_plants.html', form=form)

@app.route('/gardener/api/v1.0/setWatered', methods=['PUT'])
def set_plant_watered():
    print(request.json)
    if not request.json or not "name" in request.json:
        abort(400)
    name = request.json['name']
    p = Plant.query.filter_by(name=name).first()
    if not p:
        return jsonify({'response': 'Plant not found'}), 404
    p.last_watered = datetime.utcnow()
    db.session.commit()
    return jsonify({"response": "Done"})

