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
