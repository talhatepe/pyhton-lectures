import sqlite3

conn = sqlite3.connect("hashs.db")
c = conn.cursor()
c.execute("select * from hashTable")
print(c.fetchall())

