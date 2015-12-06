import sqlite3
from models.model import Model
from models.cookie import Cookie
from models.distributor import Distributor
from models.warehouse import Warehouse
from models.buyer import Buyer
from models.transaction import Transaction
from models.order import Order
from models.purchase import Purchase

Model.connect('CookieMonster.sqlite')
cursor = Model.cursor

cursor.execute('DELETE FROM cookies')
cursor.execute('DELETE FROM distributors')
cursor.execute('DELETE FROM warehouses')
cursor.execute('DELETE FROM buyers')
cursor.execute('DELETE FROM buyer_orders')
cursor.execute('DELETE FROM purchases')

#create cookies
for i in range(5):
  Cookie("Cookie " + str(i), 1.99).save()

#create distributors
for i in range(5):
  Distributor("Distributor " + str(i), "Somewhereville").save()

#create warehouses
for i in range(5):
  Warehouse("Warehouse " + str(i), "In a town").save()

#create buyers
for i in range(5):
  Buyer("Buyer " + str(i), "Fredmeyer").save()

#add distributor transactions
Transaction("Distributor 1", "Warehouse 1", "Cookie 1", 500, 500).save()

#add buyer order
purchase = Purchase("Cookie 1", "Warehouse 1", 5)
Order("Buyer 1", [purchase]).save()