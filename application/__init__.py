from flask import Flask
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__, static_url_path='/static')
Bootstrap(app)

from .main import main as main_blueprint
from .cookies import cookies as cookies_blueprint
from .distributors import distributors as distributors_blueprint
from .warehouses import warehouses as warehouses_blueprint
from .buyers import buyers as buyers_blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(cookies_blueprint)
app.register_blueprint(distributors_blueprint)
app.register_blueprint(warehouses_blueprint)
app.register_blueprint(buyers_blueprint)