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

@warehouses.route('/warehouses/<name>', methods=['GET', 'PUT', 'DELETE'])
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
    warehouses = []
    ware = cur.execute('''
    SELECT name, address
    FROM warehouses
    WHERE name = "{}"
    '''.format(name)).fetchone()
    print("GET", ware)
    ware = {
      "name": ware[0],
      "address" : ware[1]
    }

    cookies = []
    rows = cur.execute('''
    SELECT name, SUM(quantity)
    FROM cookies, stock
    WHERE name = cookie and warehouse = "{}"
    GROUP BY cookie
    '''.format(name))
    for r in rows:
      print("Cookie", r)
      cook = {
        "name": r[0],
        "count": r[1]
      }
      cookies.append(cook)

    ware["cookies"] = cookies
    return jsonify(**ware)

  if request.method == 'PUT':
    update = request.get_json()
    new_name = update["name"]
    address = update["address"]

    cur.execute('''
    UPDATE warehouses
    SET name = "{}", address = "{}"
    WHERE name = "{}"
    '''.format(new_name, address, name))

    cur.execute('''
    UPDATE stock
    SET warehouse = "{}"
    WHERE warehouse = "{}"
    '''.format(new_name, name))

    conn.commit()
    return jsonify(**update)

  if request.method == 'DELETE':
    cur.execute('DELETE FROM warehouses WHERE name = "{}"'.format(name))
    cur.execute('DELETE FROM stock WHERE warehouse = "{}"'.format(name))
    conn.commit()
    return "OK"