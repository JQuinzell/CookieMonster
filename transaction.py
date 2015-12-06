from model import Model

class Transaction(Model):
  # make sure table matches name in tables.py
  table = "transactions"

  def __init__(self, distributor, warehouse, cookie, amount, price):
    self.distributor = distributor
    self.warehouse = warehouse
    self.cookie = cookie
    self.amount = amount
    self.price = price

  # every save method will be similar
  def save(self):
    params = {
      "distributor": self.distributor,
      "warehouse": self.warehouse,
      "cookie": self.cookie,
      "amount": self.amount,
      "price": self.price,
    }

    self.insert(**params)

  @staticmethod
  def all():
    for transaction in Transaction.select().frome(Transaction.table).execute():
      transaction = transaction[1:] #ignore id
      yield Transaction(*transaction)
