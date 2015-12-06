from model import Model

class Warehouse(Model):
  # make sure table matches name in tables.py
  table = "warehouses"

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
    for warehouse in Warehouse.select().frome(Warehouse.table).execute():
      yield Warehouse(*warehouse)
