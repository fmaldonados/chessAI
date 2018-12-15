"""Flask Email notification."""
from flask import Flask
from flask_cors import CORS
from api import api_bp
import pymongo

def create_app():
    app = Flask(__name__)

    URI = "mongodb://proyecto:1g1bO6iQ6iotdK3ncd5f3ud5YPmTCACu19ugCeoXLjuF3Zjciqygzlu7wu8exeNq9z7CuT4V4URNdPeEjAVrcw==@proyecto.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
    client = pymongo.MongoClient(URI)
    app.DB = client["chess"]
    print ("Connected to Database")
    CORS(app)
    app.register_blueprint(api_bp)
    @app.route('/')
    def hello():
        """Simple Hello world."""
        return 'Hello World!'
    return app

APP = create_app()