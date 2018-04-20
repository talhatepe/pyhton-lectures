import sqlite3

if __name__ == "__main__":
    while True:
        conn = sqlite3.connect("hashs.db")
        cur = conn.cursor()
        value = input(str("Hash Girin: "))
        cur.execute("SELECT * FROM hashTable WHERE hash=?", (value,))
        print(cur.fetchone())
        conn.close()
