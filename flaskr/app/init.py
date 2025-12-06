from flask import Flask

app = Flask(__name__)

from .routes import init_routes
init_routes(app)
