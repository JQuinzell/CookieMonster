from . import warehouses
from flask import render_template

@warehouses.route('/warehouses')
def index():
  wares = [
    {
      "name": "Store 1",
      "address": "Place 1"
    },
    {
      "name": "Store 2",
      "address": "Place 2"
    }
  ]

  return render_template('warehouses/index.html', warehouses=wares)