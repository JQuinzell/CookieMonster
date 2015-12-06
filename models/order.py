from models.model import Model
from models.buyer import Buyer
from models.purchase import Purchase

class Order(Model):
  # make sure table matches name in tables.py
  table = "buyer_orders"

  def __init__(self, buyer, purchases):
    # get buyer id from name provided
    buyer = Buyer.select("id").frome(Buyer.table).where(first = buyer).execute().fetchone()[0]
    self.buyer = buyer
    self.purchases = purchases

  # every save method will be similar
  def save(self):
    params = {
      "buyer": self.buyer
    }

    self.insert(**params)
    order_id = Model.lastrowid()

    for purchase in self.purchases:
      purchase.order = order_id
      purchase.save()