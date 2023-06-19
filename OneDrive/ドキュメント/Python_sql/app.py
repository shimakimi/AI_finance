import sqlite3

con = sqlite3.connect('transaction.db')
cur = con.cursor()
for row in cur.execute('SELECT * FROM order_details'):
  print(row)