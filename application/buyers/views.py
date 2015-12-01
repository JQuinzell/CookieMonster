from . import buyers
from flask import render_template

@buyers.route('/buyers')
def index():
  return render_template('buyers/index.html', buyers=[])

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
  return render_template('buyers/show.html', buyer=buyer)