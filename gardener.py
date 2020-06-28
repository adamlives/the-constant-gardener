from app import app, db
from app.models import Plant, Watering

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Plant': Plant, 'Watering': Watering}