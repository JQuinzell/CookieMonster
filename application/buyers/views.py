from . import buyers
from flask import render_template, jsonify

@buyers.route('/buyers')
def index():
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

@buyers.route('/buyers/<name>')
def show(name):
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