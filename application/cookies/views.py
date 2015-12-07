from . import cookies
from model import Model
from flask import render_template, request, jsonify

@cookies.route('/cookies', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    conn, cur = Model.make_cursor()
    rows = cur.execute('''
    SELECT name, price, SUM(quantity)
    FROM cookies, stock
    WHERE name=cookie and quantity > 0
    GROUP BY cookie
    ''')

    cookies = []
    for r in rows:
      r = {
        "name": r[0],
        "price": r[1],
        "count": r[2]
      }
      cookies.append(r)

    return render_template('cookies/index.html', cookies=cookies)

  if request.method == 'POST':
    cookie = request.get_json()
    name = cookie["name"]
    price = cookie["price"]
    conn, cur = Model.make_cursor()
    cur.execute('''
    INSERT INTO cookies(name, price)
    VALUES ("{}", {})
    '''.format(name, price))
    conn.commit()
    return "OK"

@cookies.route('/cookies/<name>', methods=['GET', 'PUT', 'DELETE'])
def cookie(name):
  conn, cur = Model.make_cursor()

  if request.method == 'GET':
    row = cur.execute('''
    SELECT name, price
    FROM cookies
    WHERE name="{}"
    '''.format(name)).fetchone()

    cookie = {
      "name": row[0],
      "price": row[1]
    }

    return jsonify(**cookie)

  if request.method == 'PUT':
    #update
    cookie = request.get_json()
    new_name = cookie["name"]
    price = cookie["price"]
    cur.execute('''
    UPDATE cookies
    SET name = "{}", price = {}
    WHERE name="{}"
    '''.format(new_name, price, name))

    #also update stock references
    cur.execute('''
    UPDATE stock
    SET cookie = "{}"
    WHERE cookie = "{}"
    '''.format(new_name, name))
    conn.commit()
    return "OK"

  if request.method == 'DELETE':
    conn, cur = Model.make_cursor()
    cur.execute('DELETE FROM cookies WHERE name = "{}"'.format(name))
    conn.commit()
    return "OK"