from . import distributors
from flask import render_template, request, jsonify

@distributors.route('/distributors', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    dists = [
      {
        "name": "Guy 1",
        "address": "Place 1"
      },
      {
        "name": "Guy 2",
        "address": "Place 2"
      }
    ]
    return render_template('distributors/index.html', distributors=dists)

  if request.method == 'POST':
    dist = request.get_json()
    return jsonify(**dist)

@distributors.route('/distributors/<name>', methods=['GET', 'PUT'])
def dist(name):
  if request.method == 'GET':
    dist = {
      "name": name,
      "address": "Earth",
      "transactions": [
        {
          "id": 1,
          "price": "500",
          "cookie": "Chocolate Chip"
        },
        {
          "id": 2,
          "price": "300",
          "cookie": "Oatmeal Grossness"
        }
      ]
    }

    return jsonify(**dist)

  if request.method == 'PUT':
    update = request.get_json()
    return jsonify(**update)