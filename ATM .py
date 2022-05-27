
# print("Welcome to SBI")
# print("insert your card")
# card=int(input("select your card 1.ATM card 2.credit card:"))
# if card=="credit card" or "debit card" :
#     print("Next")
#     language=int(input("select your language 1.english 2.hindi:"))
#     if language=="1":
#         account=int(input("select your card:"))
#         if account=="1" or account=="2":
#             tranction=int(input("choose your tranction 1.balance enquiry 2.money withdrawl:"))
#             if tranction=="1" or tranction=="2":
#                 pin=int(input("enter your pin"))
#                 if pin=="****":
#                     print("1.amount enquiry")
#                          ("2.cash withdrawl")
#                          ("3.deposite")
#                          ("4.exit")
#                 else:
#                     print("invalid pin")
#             else:

# print("Welcome to SBI")
# balance=500000
# print("insert your card")
# card=int(input("select your card 1.debit card 2.credit card:"))
# if card=="credit card" or "debit card" :
#     print("Next")
#     language=int(input("select your language 1.english 2.hindi:"))
#     if language==1:
#         account=int(input("select your account 1.current account 2.saving account:"))
#         if account=="1" or "2":
#             tranction=int(input("choose your tranction 1.balance enquiry 2.money withdrawl:"))
#             if tranction=="1":
#                 print("")
#                 pin=int(input("enter your pin"))
#                 if pin==pin:
#                     print("your total amount is :",balance)
#                     # if tranction=="2":
#                     #     print("money withdrawl")
#                     # else:
#                     #      print("no money")
#                 else:
#             else:
#                  print("please chose valid transtion")
#         else: 
#             print("invalid account")
#     else:
#         ("choose another language")




print("welcome to state bank of india")
# print("swipe your card:")
card=input("enter your card:")
if card=="atm" :
    print("in process")
    language=input("enter the language :")
    if language=="english":
        print("in process")
        pin=int(input("enter the pin:"))
        if pin==1 or 1000:
            print("in process")
            type=(input("enter the type:"))
            if type=="current account" or "saving account":
                print("loading")
                trans=input("enter the transtion :")
                if trans=="withdrawl":
                    print("please wait")
                    balance=10000
                    enquiry=int(input(""))
                    amount=balance
                    if enquiry=="amount enquiry" :
                        print("your balance is",balance)
                        balance=50000
                        if balance>=0 and balance<=10000:
                            print("you can take money")
                            totalamount=int(input("enter you total amount:"))
                            print(totalamount-balance,"is remain")
                            recepit=input("did you want recpit or not:")
                            if recepit==("yes"):
                                print("take a printed recepit,if needed")
                                print("ok your withdrawl successful thank you so much")
                        else:
                           print("invalid")
                    else:
                        print("no")
                if trans=="balance enquiry":
                    print("please wait")
                else:
                    print("you cant take money")
            else:
                print("incorrect process")
        else:
            print("not answered")
    else:
        print("out process")
else:
    print("no response")
exit("out of process") 





            


                


    
        

        

