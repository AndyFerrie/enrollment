from flask import Flask
from flask_mongoengine import MongoEngine
from flask_restplus import Api

from config import Config

api = Api()

app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)
api.init_app(app)
