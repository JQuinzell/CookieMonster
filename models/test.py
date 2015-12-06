import sqlite3
import traceback
from models.model import Model
from models.cookie import Cookie
from models.distributor import Distributor
from models.warehouse import Warehouse
from models.buyer import Buyer
from models.transaction import Transaction
from models.order import Order
from models.purchase import Purchase


Model.connect('CookieMonster.sqlite')
Model.cursor.execute('PRAGMA foreign_keys=on')
cursor = Model.cursor

for cookie in Cookie.all():
  print(cookie.name, cookie.price)

for dist in Distributor.all():
  print(dist.name, dist.address)

for ware in Warehouse.all():
  print(ware.name, ware.address)

for buyer in Buyer.all():
  print(buyer.first, buyer.last)

for trans in Transaction.all():
  print(trans.distributor, trans.warehouse, trans.cookie, trans.price, trans.amount)

rows = Model.cursor.execute('SELECT * FROM cookies')

for row in rows:
  print(row)