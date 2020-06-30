from app import app, db
from app.models import User, Plant, Watering

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Plant': Plant, 'Watering': Watering}