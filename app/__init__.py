from flask import Flask
from .routes import main
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.register_blueprint(main)

    return app