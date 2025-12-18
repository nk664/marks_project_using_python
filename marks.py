import sqlite3
while True:
    print("\n\n========== SCHOLR ===========\n\n")
    
    # registration or login for teacher or staff
    
    print("1. Register your self only for teachers if not registred\n")
    print("2. Login if registred\n")
    choice = int(input("Enter your choice:- "))
    
# registration

    if choice == 1:
        while True:
            name = input("Enter your name:- ").strip()
            length =  len(name)
            if length <3 or length > 20:
                print("Name should be more then 3 letters and less then 20")
            else:
                phone = (input("Enter your phone number:- "))
                length =  len(phone)
            if length != 10 or not phone.isdigit():
                 print("enter a valid phone number")
            else:
                email = input("Enter your mail").strip()
                passward = input("Set your passward").strip()
                continue
        
# login

    elif choice == 2:
        phone = int(input("Enter your phone number"))
        passward = input("Enter your passward").strip()

    elif choice <1 or choice >2:
         print("You have entered an invalid choice")
    