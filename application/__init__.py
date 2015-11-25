from flask import Flask
app = Flask(__name__, static_url_path='/static')

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)