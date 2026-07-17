print("welcome to atm")
print("please insert your card")
username = 'dhanush'
password = 'dhanush123'
username = input("enter your name:")
password = str(input("enter your password"))
if username == username and password == password:
    print("welcome to atm service")
    print("select your language:")
    print('''
          1. english
          2. hindi
          3. telugu
          ''')
    lang = int(input("select your language:"))
    if lang == 1:
            print("you have selected english")
    elif lang == 2:
            print("you have selected hindi")
    elif lang == 3:
            print("you have selected telugu")
    print("choose your service:")
    print('''
          1. balance enquiry
          2. cash withdrawl
          3. deposit
          ''')
    amount = 50000
    option = int(input("select your option:"))
    if option == 1:
        print("your balance is:", amount)
    elif option == 2:
        withdrawl = int(input("enter the amount to withdraw:"))
        if withdrawl <= amount:
            amount = amount - withdrawl
            print("please collect your cash")
            print("your remaining balance is:", amount)
        else:
            print("insufficient balance")
    elif option == 3:
        deposit = int(input("enter the amount to deposit:"))
        amount = amount + deposit
        print("your new balance is:", amount)
else:
    print("service denied")
print("please take your card")
print("thank you for using atm service")


    