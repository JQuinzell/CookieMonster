from flask import Flask
app = Flask(__name__, static_url_path='/static')

from .main import main as main_blueprint
from .cookies import cookies as cookies_blueprint
from .distributors import distributors as distributors_blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(cookies_blueprint)
app.register_blueprint(distributors_blueprint)