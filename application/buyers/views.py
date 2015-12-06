from . import buyers
from models import Model
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

    return render_template('buyers/index.html', buyers=buyers)

  if request.method == 'POST':
    buyer = request.get_json()
    #create buyer
    return jsonify(**buyer)

@buyers.route('/buyers/<int:buyer_id>', methods=['GET', 'PUT', 'DELETE'])
def show(buyer_id):
  #find buyer with buyer_id

  if request.method == 'GET':
    buyer = {
      "name": "John Doe", #first + last
      "addresses": [{"address": "Address 1"}, {"address": "Address 2"}], #use join table
      "id": buyer_id,
      "orders": [
        {
          "id": 1,
          "description": "I bought some cookies!",
          "total": 0, #aggregate - sum price
          "purchases": [
            {
              "cookie": "Test",
              "warehouse": "Some Warehouse",
              "amount": 0,
              "price": "0.00"
            },
            {
              "cookie": "Test",
              "warehouse": "Some Warehouse",
              "amount": 0,
              "price": "0.00"
            }
          ]
        },
        {
          "id": 2,
          "description": "I bought some cookies!",
          "total": 0,
          "purchases": [
            {
              "cookie": "Test",
              "warehouse": "Some Warehouse",
              "amount": 0,
              "price": "0.00"
            },
            {
              "cookie": "Test",
              "warehouse": "Some Warehouse",
              "amount": 0,
              "price": "0.00"
            }
          ]
        }
      ]
    }
    return jsonify(**buyer)

  if request.method == 'PUT':
    update = request.get_json()
    first, last = update["name"].split(" ")
    #update buyer with this information
    update = {
      "first": first,
      "last": last,
    }
    return jsonify(**update)

  if request.method == 'DELETE':
    #delete buyer with id = buyer_id
    return "OK"