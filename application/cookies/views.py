from . import cookies
from flask import render_template, request, jsonify

@cookies.route('/cookies', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    cookies = [
      {
        "name": "Chocolate Chip",
        "price": "5.99",
        "count": 5
      },
      {
        "name": "Yo Mama",
        "price": "11.59",
        "count": 200
      }
    ]
    return render_template('cookies/index.html', cookies=cookies)

  if request.method == 'POST':
    cookie = request.get_json()
    return jsonify(**cookie)

@cookies.route('/cookies/<name>', methods=['GET', 'PUT'])
def cookie(name):
  if request.method == 'GET':
    cookie = {
      "name": name,
      "price": "5.99"
    }

    return jsonify(**cookie)

  if request.method == 'PUT':
    #update
    update = request.get_json()
    return jsonify(**update)