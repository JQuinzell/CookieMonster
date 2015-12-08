from . import main
from flask import render_template
from model import Model

@main.route('/')
def index():
  conn, cur = Model.make_cursor()
  stats = {}

  total = cur.execute('''
  SELECT SUM(quantity)
  FROM stock
  WHERE quantity > 0
  ''').fetchone()[0]

  purchases = cur.execute('''
  SELECT SUM(amount)
  FROM purchases
  WHERE amount > 0
  ''').fetchone()[0]

  price = cur.execute('''
  SELECT SUM(total)
  FROM buyer_orders
  ''').fetchone()[0]

  transactions_made = cur.execute('''
  SELECT SUM(amount)
  FROM transactions
  ''').fetchone()[0]

  transactions_price = cur.execute('''
  SELECT SUM(price)
  FROM transactions
  ''').fetchone()[0]

  stats["total_cookies"] = total
  stats["total_purchases"] = purchases
  stats["total_price"] = price
  stats["transactions_made"] = transactions_made
  stats["transactions_price"] = transactions_price
  return render_template('index.html', stats=stats)

@main.route('/static/<path:path>')
def asset(path):
  return current_app.send_static_file(path)