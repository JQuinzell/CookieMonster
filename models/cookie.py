from models.model import Model

class Cookie(Model):
  # make sure table matches name in tables.py
  table = "cookies"

  def __init__(self, name, price, theme=None, diameter=None):
    self.name = name
    self.theme = theme
    self.price = price
    self.diameter = diameter

  # every save method will be similar
  def save(self):
    params = {
      "name": self.name,
      "price": self.price,
    }

    #only add if attribute is not None (null)
    if self.theme:
      params["theme"] = self.theme

    if self.diameter:
      params["diameter"] = self.diameter

    self.insert(**params)

  @staticmethod
  def all():
    for cookie in Cookie.select().frome(Cookie.table).execute():
      yield Cookie(*cookie)
