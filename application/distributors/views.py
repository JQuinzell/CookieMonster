from . import distributors
from flask import render_template, request, jsonify
from model import Model

@distributors.route('/distributors', methods=['GET', 'POST'])
def index():
  conn, cur = Model.make_cursor()
  if request.method == 'GET':
    dists = []
    rows = cur.execute('''
    SELECT name, address
    FROM distributors
    ''')
    for r in rows:
      d = {
        "name": r[0],
        "address": r[1]
      }
      dists.append(d)

    return render_template('distributors/index.html', distributors=dists)

  if request.method == 'POST':
    dist = request.get_json()
    name = dist["name"]
    address = dist["address"]
    cur.execute('''
    INSERT INTO distributors(name, address)
    VALUES ("{}", "{}")
    '''.format(name, address))
    conn.commit()
    return jsonify(**dist)

@distributors.route('/distributors/<name>', methods=['GET', 'PUT'])
def dist(name):
  if request.method == 'GET':
    conn, cur = Model.make_cursor()
    dist = cur.execute('SELECT name, address FROM distributors WHERE name="{}"'.format(name)).fetchone()
    dist = {
      "name": dist[0],
      "address": dist[1]
    }

    transactions = []
    rows = cur.execute('''
    SELECT id, price, cookie, amount
    FROM transactions
    WHERE distributor = "{}"
    '''.format(name))
    for r in rows:
      trans = {
        "id": r[0],
        "price": r[1],
        "cookie": r[2],
        "amount": r[3]
      }
      transactions.append(trans)

    dist["transactions"] = transactions
    return jsonify(**dist)

  if request.method == 'PUT':
    update = request.get_json()
    return jsonify(**update)