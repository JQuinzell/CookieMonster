import sqlite3

conn = sqlite3.connect('CookieMonster.sqlite')
conn.execute('PRAGMA foreign_keys=on')
cursor = conn.cursor()

cursor.execute('''
  CREATE TABLE IF NOT EXISTS cookies(
    name VARCHAR(20),
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
    address VARCHAR(20),
    PRIMARY KEY(address)
  );
  ''')

cursor.execute('''
  CREATE TABLE IF NOT EXISTS sells(
    distributor VARCHAR(20) REFERENCES distributors(name),
    cookie VARCHAR(20) REFERENCES cookies(name),
    price INTEGER
  );
  ''')

cursor.execute('''
  CREATE TABLE IF NOT EXISTS stock(
    cookie VARCHAR(20) REFERENCES cookies(name),
    warehouse VARCHAR(20) REFERENCES warehouses(address),
    quantity INTEGER NOT NULL,
    PRIMARY KEY(cookie, warehouse)
  );
  ''')

cursor.execute('''
  CREATE TABLE IF NOT EXISTS buyers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first VARCHAR(20),
    middle VARCHAR(20),
    last VARCHAR(20),
    phone CHAR(10)
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

cursor.execute('''
  CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    buyer INTEGER REFERENCES buyers(id),
    description TEXT
  );
  ''')

conn.commit()