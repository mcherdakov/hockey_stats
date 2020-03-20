import pandas as pd
from hockey_stats_backend.api.models import Player
from hockey_stats_backend.api import db
from hockey_stats_backend.api import create_app

app = create_app()
app.run()

df = pd.read_csv('player.csv')

to_db = 50

players = []
for index, row in df.iterrows():
    if len(players) > to_db:
        break

    players.append(Player(name=row['name']))

db.session.add_all(players)
db.session.commit()

