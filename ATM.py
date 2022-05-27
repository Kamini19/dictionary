print("welcome to SBI :")
a=input("select your language :")
if a=="English":
    print("English")
    print("Ok then Next go")
    print("please swipe your card")
print("please enter your best pin")
B=int(input("**"))
if (B>=0000 or B==1234) and (B<=9999 or B==4567):
    print('''1 Amount Enquiry
           2  Cash withdrawl
           3  Deposite
           4  exit''')
else:
     print("invalid pin")
balance=10000
Enquiry=int(input(""))
Amount=balance
if Enquiry==1:
    print("Your balance is",balance)
elif Enquiry==2:
    wid=int(input("Please Enter Your Amount"))             
    print("Your Balance is",balance-wid)
    print("please collect your Amount -  ")
elif Enquiry==3:
    print("previous amount is",balance)
    Dep=int(input("enter your deposit amount"))
    print("your deposit amount is ",balance+Dep)
elif Enquiry==4:
    print("Thanks for visiting SBI")
    exit()
    
