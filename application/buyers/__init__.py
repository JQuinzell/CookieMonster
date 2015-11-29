from flask import Blueprint

buyers = Blueprint('buyers', __name__)

from . import views