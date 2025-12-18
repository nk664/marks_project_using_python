import sqlite3
con = sqlite3.connect("bank.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS usres(acc_no, pin, phone, name, amount)")
cur.execute("ALTER TABLE usres RENAME TO users")
con.commit()
con.close()
print("haa table ban gaYA")