from flask import Blueprint
from flask_restful import Api
from api.Match import Match
from api.Hello import Hello



api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Hello, '/hello')
api.add_resource(Match, '/match')