import sqlite3

conn = sqlite3.connect('CookieMonster.sqlite')
conn.execute('PRAGMA foreign_keys=on')
cursor = conn.cursor()

cursor.execute('''
  CREATE TABLE IF NOT EXISTS cookies(
    name VARCHAR(20),
    price REAL,
    theme VARCHAR(20),
    diameter INTEGER,
    PRIMARY KEY(name)
  );
  ''')

cursor.execute('''
  CREATE TABLE IF NOT EXISTS distributors(
    name VARCHAR(20),
    address VARCHAR(20),
    PRIMARY KEY(name)
  );
  ''')

cursor.execute('''
  CREATE TABLE IF NOT EXISTS warehouses(
    name VARCHAR(20),
    address VARCHAR(20),
    PRIMARY KEY(name)
  );
  ''')

cursor.execute('''
  CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    distributor VARCHAR(20) REFERENCES distributors(name),
    cookie VARCHAR(20) REFERENCES cookies(name),
    warehouse VARCHAR(20) REFERENCES warehouses(name),
    price REAL,
    amount int
  );
  ''')

cursor.execute('''
  CREATE TABLE IF NOT EXISTS stock(
    cookie VARCHAR(20) REFERENCES cookies(name),
    warehouse VARCHAR(20) REFERENCES warehouses(name),
    quantity INTEGER NOT NULL,
    PRIMARY KEY(cookie, warehouse)
  );
  ''')

cursor.execute('''
  CREATE TABLE IF NOT EXISTS buyers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first VARCHAR(20),
    last VARCHAR(20)
  );
  ''')

cursor.execute('''
  CREATE TABLE IF NOT EXISTS addresses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    line1 VARCHAR(20),
    line2 VARCHAR(20),
    state CHAR(2),
    street VARCHAR(20)
  );
  ''')

cursor.execute('''
  CREATE TABLE IF NOT EXISTS buyers_addresses(
    buyer INTEGER REFERENCES buyers(id),
    address INTEGER REFERENCES addresses(id),
    PRIMARY KEY(buyer, address)
  );
  ''')

#buyer_orders because order is a keyword
cursor.execute('''
  CREATE TABLE IF NOT EXISTS buyer_orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    buyer INTEGER REFERENCES buyers(id),
    description TEXT,
    total REAL
  );
  ''')

cursor.execute('''
  CREATE TABLE IF NOT EXISTS purchases(
    cookie VARCHAR(20) REFERENCES cookies(name),
    warehouse VARCHAR(20) REFERENCES warehouses(name),
    buyer_order INTEGER REFERENCES buyer_orders(id),
    amount INTEGER,
    PRIMARY KEY(cookie, warehouse, buyer_order)
  );
  ''')

conn.commit()