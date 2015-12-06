from . import buyers
from model import Model
from flask import render_template, jsonify, request

@buyers.route('/buyers', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    buyers = []
    for buyer in Model.execute('SELECT first, last, id FROM buyers'):
      buyer = {
        "name": "{} {}".format(buyer[0], buyer[1]),
        "id": buyer[2]
      }
      buyers.append(buyer)
      print("INDEX BUYER:", buyer)
    return render_template('buyers/index.html', buyers=buyers)

  if request.method == 'POST':
    buyer = request.get_json()
    first, last = buyer["name"].split()
    Model.insert_in("buyers", first=first, last=last)
    #create buyer
    return jsonify(**buyer)

@buyers.route('/buyers/<int:buyer_id>', methods=['GET', 'PUT', 'DELETE'])
def show(buyer_id):
  #find buyer with buyer_id

  if request.method == 'GET':
    buyer = Model.execute('SELECT first, last, id FROM buyers WHERE id={}'.format(buyer_id)).fetchone()
    print("GET BUYER:", buyer)
    buyer = {
      "name": "{} {}".format(buyer[0], buyer[1]),
      "id": buyer[2]
    }

    orders = []
    for order in Model.execute('SELECT id, buyer, description, total FROM buyer_orders WHERE buyer={}'.format(buyer_id)):
      print("ORDER:", order)
      oid = order[0]
      order = {
        "id": order[0],
        "description": order[2],
        "total": order[3]
      }

      purchases = []
      for p in Model.execute('SELECT cookie, warehouse, buyer_order, amount FROM purchases WHERE buyer_order={}'.format(oid)):
        p = {
          "cookie": p[0],
          "warehouse": p[1],
          "amount": p[3]
        }
        purchases.append(p)

      order["purchases"] = purchases
      orders.append(order)
    buyer["orders"] = orders
    return jsonify(**buyer)

  if request.method == 'PUT':
    update = request.get_json()
    first, last = update["name"].split(" ")
    #update buyer with this information
    conn, cur = Model.make_cursor()
    cur.execute('''
    UPDATE buyers
    SET first="{}", last="{}"
    WHERE id={}
    '''.format(first, last, buyer_id))
    conn.commit()
    return "OK"

  if request.method == 'DELETE':
    #delete buyer with id = buyer_id
    conn, cur = Model.make_cursor()
    cur.execute('DELETE FROM buyers WHERE id={}'.format(buyer_id))
    conn.commit()
    return "OK"