from flask import Blueprint

distributors = Blueprint('distributors', __name__)

from . import views