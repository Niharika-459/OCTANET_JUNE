import time
print("***please insert  your card***\n keep your card inserted until transaction completes***")
time.sleep(5)
password=1234
pin=int(input("enter your  pin"))
balance=5000
if pin==password:
    while True:
        print ("""
            1 == balance enquiry
            2 == withdraw cash
            3 == deposit cash
            4 == exit
            """
            )
        
        try:
            option=int(input("please enter your choice"))
        except:
            print("please enter valid input")

        if option==1:
                print(f"your balnce is:{balance}")
        if option==2:
                withdraw_amount=int(input("please enter the amount"))
                balance=balance-withdraw_amount
                print(f"{withdraw_amount} is debited from your account")
                print(f"your updated balance is:{balance}")
        if option==3:
                    deposit_amount=int(input("please enter the amount"))
                    balance=balance+deposit_amount
                    print(f"{deposit_amount} is credited to your account")
                    print(f"your updated balance is{balance}")
        if option==4:
                    print(f"THANK YOU!!!")
                    break
    pass
else:
    print("incorrect pin try again")