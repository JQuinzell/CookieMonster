from . import warehouses
from flask import render_template, jsonify, request

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

@warehouses.route('/warehouses/<name>', methods=['GET', 'PUT'])
def warehouse(name):
  if request.method == 'GET':
    ware = {
      "name": name,
      "address": "Near walmart",
      "cookies": [
        {
          "name": "Cookie Dough",
          "count": 100
        },
        {
          "name": "Something Good",
          "count": 1000
        }
      ]
    }

    return jsonify(**ware)

  if request.method == 'PUT':
    update = request.get_json()
    return jsonify(**update)