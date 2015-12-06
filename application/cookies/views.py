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
    WHERE name=cookie
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

@cookies.route('/cookies/<name>', methods=['GET', 'PUT'])
def cookie(name):
  if request.method == 'GET':
    #not in use
    cookie = {
      "name": name,
      "price": "5.99"
    }

    return jsonify(**cookie)

  if request.method == 'PUT':
    #update
    update = request.get_json()
    return jsonify(**update)