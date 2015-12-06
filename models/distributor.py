from models.model import Model
from models.transaction import Transaction

class Distributor(Model):
  # make sure table matches name in tables.py
  table = "distributors"

  def __init__(self, name, address):
    self.name = name
    self.address = address

  # every save method will be similar
  def save(self):
    params = {
      "name": self.name,
      "address": self.address
    }

    self.insert(**params)

  @staticmethod
  def all():
    for distributor in Distributor.select().frome(Distributor.table).execute():
      yield Distributor(*distributor)
