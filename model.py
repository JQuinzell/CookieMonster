import sqlite3
from query import Query

class Model(object):

  def __init__(self):
    pass

  @staticmethod
  def connect(uri):
    Model.uri = uri
    Model.conn = sqlite3.connect(uri)
    Model.cursor = Model.conn.cursor()

  @staticmethod
  def execute(sql):
    conn = sqlite3.connect(Model.uri)
    cursor = conn.cursor()
    return cursor.execute(sql)

  @staticmethod
  def insert_in(table, **params):
    attributes = "(" + ", ".join('"{0}"'.format(w) for w in params.keys()) + ")"
    values = "(" + ", ".join('"{0}"'.format(w) for w in params.values()) + ")"

    sql = "INSERT INTO " + table + attributes + " VALUES " + values
    conn = sqlite3.connect(Model.uri)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

  def insert(self, **params):
    attributes = "(" + ", ".join('"{0}"'.format(w) for w in params.keys()) + ")"
    values = "(" + ", ".join('"{0}"'.format(w) for w in params.values()) + ")"

    sql = "INSERT INTO " + self.table + attributes + " VALUES " + values
    Model.cursor.execute(sql)
    Model.conn.commit()

  @staticmethod
  def select(*columns):
    cursor = Model.conn.cursor()
    query = Query(cursor)

    if columns:
      query.select(*columns)
    
    return query

  @staticmethod
  def lastrowid():
    return Model.cursor.lastrowid