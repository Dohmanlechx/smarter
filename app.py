from flask import Flask
from src.routes import init_routes

app = Flask(__name__)
init_routes(app)