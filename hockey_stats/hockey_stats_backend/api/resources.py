from flask_restful import Resource
from hockey_stats_backend.api.models import Player
from hockey_stats_backend.api.serializers import PlayersSerializer


class Players(Resource):
    def get(self):
        players = Player.query.all()
        data = PlayersSerializer(players).serialize()
        return data
