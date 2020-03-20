class PlayersSerializer:
    def __init__(self, players_query):
        self.query = players_query

    def serialize(self):
        data = []
        for player in self.query:
            data.append({
                'id': player.id,
                'name': player.name,
            })
        return data
