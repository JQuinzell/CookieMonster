import sqlite3

class Model(object):
  def __init__(self):
    pass

  @staticmethod
  def connect(uri):
    Model.conn =sqlite3.connect(uri)
    Model.cursor = Model.conn.cursor()

  def insert(self, params):
    attributes = "(" + ", ".join('"{0}"'.format(w) for w in params.keys()) + ")"
    values = "(" + ", ".join('"{0}"'.format(w) for w in params.values()) + ")"

    sql = "INSERT INTO " + self.table + attributes + " VALUES " + values
    Model.cursor.execute(sql)
    Model.conn.commit()

