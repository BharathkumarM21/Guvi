import re,random 
while True:
    mail=input("Enter Email-Id: ")
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex,mail)):  
        break  
    else:  
        print("Invalid Email")
        continue
while True:
  mobileno=input("Enter MobileNumber:")
  if len(mobileno)!=10 or mobileno[0]!="9":
    print("Sorry, Obtain 10 numbers")
    continue
  else:
     break
while True:
    password=input("Enter Password:")
    if re.match(r'[A-Za-z0-9@#$%^&+=]{6,}', password):
        class Account:
            def __init__(a):
                a.balance=0
            def deposit(a):
                amount=float(input("Amount to be Deposited: "))
                a.balance += amount
                print("\n Amount Deposited:",amount)
            def withdraw(a):
                amount = float(input("Amount to be Withdrawn: "))
                if a.balance>=amount:
                    a.balance-=amount
                    print("\n You Withdrew:", amount)
                else:
                    print("\n Invalid Deposited amount  ")
            def display(a):
                print("\n Net Available Balance=",a.balance)
        s = Account()
        s.deposit()
        s.withdraw()
        s.display()
    else:
        print("Password must contain atleast 6 letters and should contain 1Number,1Capital & 1SpecialCharacter")
        continue
