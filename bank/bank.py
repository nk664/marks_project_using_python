import sqlite3
def get_user(acc):
  con = sqlite3.connect("bank.db")
  cur = con.cursor()
  cur.execute("SELECT * FROM users WHERE "(acc_no, pin, phone, name, amount))
  con.commit()
  con.close()
  return data
def insert(acc_no, pin, phone, name, amount):
  con = sqlite3.connect("bank.db")
  cur = con.cursor()
  cur.execute("INSERT INTO users (acc_no, pin, phone, name, amount) VALUES (?, ?, ?, ?, ?)",(acc_no, pin, phone, name, amount))
  con.commit()
  con.close()
  print(f"account created successfully : \n account no: {acc_no}\n phone no: {phone}\n name: {name}\n amount: {amount}")

print("=======ATM========")
print("=======MENU=======")
print("1. login")
print("2. create new account ")
print("3. logout")
while True:
      choice = int(input("enter your choice "))
      if choice == 1:
        acc = (input("enter your account no"))
        get_user(acc)
        if pin == "users[1]":
           print("1. check balance")
           print("2. deposit money")
           print("3. withdraw money")
           print("4. logout")
        else:
           print("invalid pin")
      elif choice == 2:
        name = (input("enter your name: "))
        acc_no = (input("enter your account no.: "))  
        pin  = (input("set your pin: ")) 
        phone = (input("ph. no: ")) 
        amount = (input("balance: ")) 
        insert(acc_no,  pin, phone, name, amount)
      elif choice == 3:
         

