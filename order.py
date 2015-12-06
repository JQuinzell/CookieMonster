from model import Model
from buyer import Buyer
from purchase import Purchase

class Order(Model):
  # make sure table matches name in tables.py
  table = "buyer_orders"

  def __init__(self, buyer, total, purchases):
    # get buyer id from name provided
    buyer = Buyer.select("id").frome(Buyer.table).where(first = buyer).execute().fetchone()[0]
    self.buyer = buyer
    self.total = total
    self.purchases = purchases

  # every save method will be similar
  def save(self):
    params = {
      "buyer": self.buyer,
      "total": self.total
    }

    self.insert(**params)
    order_id = Model.lastrowid()

    for purchase in self.purchases:
      purchase.order = order_id
      purchase.save()