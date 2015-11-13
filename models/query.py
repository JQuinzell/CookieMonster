class Query(object):
  def __init__(self, cursor):
    self.columns = []
    self.tables = []
    self.conditions = []
    self.cursor = cursor

  def select(self, *columns):
    if columns: 
      self.columns.extend(columns)
    return self

  def frome(self, *tables):
    if tables:
      self.tables.extend(tables)
    return self

  def where(self, **conditions):
    sql = ", ".join(self.sanitize(w) for w in conditions.items())
    self.conditions.append(sql)
    return self

  def execute(self):
    select_clause = "SELECT "
    if not self.columns:
      select_clause += "* "
    else:
      select_clause += ", ".join(self.columns)

    from_clause = "FROM " + ", ".join(self.tables)

    where_clause = ""
    if self.conditions:
      where_clause = " WHERE " + " and ".join(self.conditions)

    sql = select_clause + from_clause + where_clause
    return self.cursor.execute(sql)

  def sanitize(self, pair):
    return '{} = "{}"'.format(*pair)
