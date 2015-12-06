from models.model import Model

class Purchase(Model):
  # make sure table matches name in tables.py
  table = "purchases"

  def __init__(self, cookie, warehouse, amount):
    self.cookie = cookie
    self.warehouse = warehouse
    self.amount = amount
    self.order = None

  # every save method will be similar
  def save(self):
    params = {
      "cookie": self.cookie,
      "warehouse": self.warehouse,
      "amount": self.amount,
      "buyer_order": self.order,
    }

    self.insert(**params)