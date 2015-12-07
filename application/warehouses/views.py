from . import warehouses
from flask import render_template, jsonify, request
from model import Model

@warehouses.route('/warehouses', methods=['GET', 'POST'])
def index():
  conn, cur = Model.make_cursor()

  if request.method == 'GET':
    wares = []
    rows = cur.execute('''
    SELECT name, address
    FROM warehouses
    ''')
    for r in rows:
      w = {
        "name": r[0],
        "address": r[1]
      }
      wares.append(w)

    return render_template('warehouses/index.html', warehouses=wares)

  if request.method == 'POST':
    ware = request.get_json()
    name = ware["name"]
    address = ware["address"]
    cur.execute('''
    INSERT INTO warehouses(name, address)
    VALUES ("{}", "{}")
    '''.format(name, address))
    conn.commit()
    return jsonify(**ware)

@warehouses.route('/warehouses/<name>', methods=['GET', 'PUT'])
def warehouse(name):
  conn, cur = Model.make_cursor()
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