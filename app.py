"""Flask Email notification."""
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    @app.route('/')
    def hello():
        """Simple Hello world."""
        return 'Hello World!'
    return app

APP = create_app()