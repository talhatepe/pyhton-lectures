# Homework - Week 7

### • hw1.py (Create Rainbow Table):
```python
import sqlite3
import hashlib
import itertools

if __name__ == "__main__":
    conn = sqlite3.connect("hashs.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS hashTable (string text, hash text)''')
    arr = []

    for i in range(48, 58):
        arr.append(chr(i))

    for i in range(97, 123):
        arr.append(chr(i))

    for i in range(65, 91):
        arr.append(chr(i))

    for passwd in itertools.permutations(arr, r=1):
        m = hashlib.md5()
        string = str(''.join(passwd))
        m.update(string.encode('utf-8'))
        a = str(''.join(m.hexdigest()))
        print("INSERT INTO hashTable VALUES ('{0}','{1}')".format(''.join(passwd), ''.join(a)))
        cur.execute("INSERT INTO hashTable VALUES ('{0}','{1}')".format(''.join(passwd), ''.join(a)))
        conn.commit()

    for passwd in itertools.permutations(arr, r=2):
        m = hashlib.md5()
        string = str(''.join(passwd))
        m.update(string.encode('utf-8'))
        a = str(''.join(m.hexdigest()))
        print("INSERT INTO hashTable VALUES ('{0}','{1}')".format(''.join(passwd), ''.join(a)))
        cur.execute("INSERT INTO hashTable VALUES ('{0}','{1}')".format(''.join(passwd), ''.join(a)))
        conn.commit()

    for passwd in itertools.permutations(arr, r=3):
        m = hashlib.md5()
        string = str(''.join(passwd))
        m.update(string.encode('utf-8'))
        a = str(''.join(m.hexdigest()))
        print("INSERT INTO hashTable VALUES ('{0}','{1}')".format(''.join(passwd), ''.join(a)))
        cur.execute("INSERT INTO hashTable VALUES ('{0}','{1}')".format(''.join(passwd), ''.join(a)))
        conn.commit()

    for passwd in itertools.permutations(arr, r=4):
        m = hashlib.md5()
        string = str(''.join(passwd))
        m.update(string.encode('utf-8'))
        a = str(''.join(m.hexdigest()))
        print("INSERT INTO hashTable VALUES ('{0}','{1}')".format(''.join(passwd), ''.join(a)))
        cur.execute("INSERT INTO hashTable VALUES ('{0}','{1}')".format(''.join(passwd), ''.join(a)))
        conn.commit()

    for passwd in itertools.permutations(arr, r=5):
        m = hashlib.md5()
        string = str(''.join(passwd))
        m.update(string.encode('utf-8'))
        a = str(''.join(m.hexdigest()))
        print("INSERT INTO hashTable VALUES ('{0}','{1}')".format(''.join(passwd), ''.join(a)))
        cur.execute("INSERT INTO hashTable VALUES ('{0}','{1}')".format(''.join(passwd), ''.join(a)))
        conn.commit()

    for passwd in itertools.permutations(arr, r=6):
        m = hashlib.md5()
        string = str(''.join(passwd))
        m.update(string.encode('utf-8'))
        a = str(''.join(m.hexdigest()))
        print("INSERT INTO hashTable VALUES ('{0}','{1}')".format(''.join(passwd), ''.join(a)))
        cur.execute("INSERT INTO hashTable VALUES ('{0}','{1}')".format(''.join(passwd), ''.join(a)))
        conn.commit()

    conn.close()

```

> 1,2,3,4,5 ve 6'lı permutasyonlar ile hashlerini veritabanına kayıt eder.


### • hw2.py (Search hash in Database):
```python
import sqlite3

if __name__ == "__main__":
    while True:
        conn = sqlite3.connect("hashs.db")
        cur = conn.cursor()
        value = input(str("Hash Girin: "))
        cur.execute("SELECT * FROM hashTable WHERE hash=?", (value,))
        print(cur.fetchone())
        conn.close()

```

> Veritabanında bulunan hashTable adlı tabloda girilen hashi arar bulursa karşılığı olan stringi ve hashi ekrana basar.


### • hw3.py (Database Dump):
```python
import sqlite3

conn = sqlite3.connect("hashs.db")
c = conn.cursor()
c.execute("select * from hashTable")
print(c.fetchall())

```

> Veritabanında bulunan hashTable adlı tabloda ki tüm veriyi ekrana basar.