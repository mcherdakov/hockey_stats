from flask import Blueprint
from flask_restful import Api

from hockey_stats_backend.api import resources

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(resources.Players, '/players')
