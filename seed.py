import sqlite3
from model import Model
from cookie import Cookie
from distributor import Distributor
from warehouse import Warehouse
from buyer import Buyer
from transaction import Transaction
from order import Order
from purchase import Purchase

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
  Cookie("Cookie" + str(i), 1.99).save()

#create distributors
for i in range(5):
  Distributor("Distributor" + str(i), "Somewhereville").save()

#create warehouses
for i in range(5):
  Warehouse("Warehouse" + str(i), "In a town").save()

#create buyers
for i in range(5):
  Buyer("Buyer" + str(i), "Fredmeyer").save()

#add distributor transactions
Transaction("Distributor1", "Warehouse1", "Cookie1", 500, 500).save()

#add buyer order
purchase1 = Purchase("Cookie1", "Warehouse1", 5)
purchase2 = Purchase("Cookie2", "Warehouse2", 5)
Order("Buyer1", 20, [purchase1, purchase2]).save()