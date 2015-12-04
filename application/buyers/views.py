from . import buyers
from flask import render_template, jsonify, request

@buyers.route('/buyers', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    buyers = [
      {
        "name": "Buyer 1",
        "address": "Place 1"
      },
      {
        "name": "Buyer 2",
        "address": "Place 2"
      }
    ]

    return render_template('buyers/index.html', buyers=buyers)

  if request.method == 'POST':
    buyer = request.get_json()
    #create buyer
    return jsonify(**buyer)

@buyers.route('/buyers/<name>', methods=['GET', 'PUT'])
def show(name):
  if request.method == 'GET':
    buyer = {
      "name": name,
      "address": "Test",
      "orders": [
        {
          "id": 1,
          "total": 0,
          "cookies": [
            {
              "name": "Test",
              "price": "0.00"
            },
            {
              "name": "Test",
              "price": "0.00"
            }
          ]
        },
        {
          "id": 2,
          "total": 0,
          "cookies": [
            {
              "name": "Test",
              "price": "0.00"
            },
            {
              "name": "Test",
              "price": "0.00"
            }
          ]
        }
      ]
    }
    return jsonify(**buyer)

  if request.method == 'PUT':
    # Update buyer
    update = request.get_json()
    return jsonify(**update)