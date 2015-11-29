from flask import Blueprint

warehouses = Blueprint('warehouses', __name__)

from . import views