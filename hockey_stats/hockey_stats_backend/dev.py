from hockey_stats_backend.api import create_app
from hockey_stats_backend.api import db
from hockey_stats_backend.api.models import Player

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Player': Player}