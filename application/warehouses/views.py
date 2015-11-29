# from flask import send_static_file
from . import warehouses
from flask import render_template

@warehouses.route('/warehouses')
def index():
  return render_template('warehouses/index.html', warehouses=[])