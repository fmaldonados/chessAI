from flask_restful import Resource, reqparse
from flask import current_app

class Hello(Resource):
    def get(self):
        return "Welcome to the AI Chess API",202


