from model import Model

class Cookie(Model):
  # make sure table matches name in tables.py
  table = "cookies"

  def __init__(self, name, theme=None, diameter=None):
    self.name = name
    self.theme = theme
    self.diameter = diameter

  # every save method will be similar
  def save(self):
    params = {
      "name": self.name,
    }

    #only add if attribute is not None (null)
    if self.theme:
      params["theme"] = self.theme

    if self.diameter:
      params["diameter"] = self.diameter

    self.insert(**params)
