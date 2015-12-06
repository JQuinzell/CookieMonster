from models.model import Model

class Buyer(Model):
  # make sure table matches name in tables.py
  table = "buyers"

  def __init__(self, first, last):
    self.first = first
    self.last = last

  # every save method will be similar
  def save(self):
    params = {
      "first": self.first,
      "last": self.last,
    }

    self.insert(**params)

  @staticmethod
  def all():
    for buyer in Buyer.select().frome(Buyer.table).execute():
      #remove id from tuple
      buyer = buyer[1:]
      yield Buyer(*buyer)
