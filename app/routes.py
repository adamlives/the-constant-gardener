from flask import render_template

from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Seed'}
    plants = [
        {
            'name': 'Spike',
            'location': 'Back Room',
            'last_watered_time': '15:15',
            'last_watered_date': '28Jun2020'
        },
        {
            'name': 'Jonathan',
            'location': 'Hall',
            'last_watered_time': '08:30',
            'last_watered_date': '27Jun2020'
        }
    ]
    return render_template('index.html', title='The Constant Gardener', user=user, plants=plants)